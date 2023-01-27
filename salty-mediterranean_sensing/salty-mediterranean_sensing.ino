// ========== START: Imports ==========
#include <ESP8266WiFi.h>

// ----- Firebase Realtime Database -----
#include <Firebase_ESP_Client.h>
#include <addons/TokenHelper.h>
#include <addons/RTDBHelper.h>

// ----- Waterproof DS18B20 -----
#include <OneWire.h>
#include <DallasTemperature.h>

// ----- DHT22 -----
#include "DHT.h"

// ----- NTP Client -----
#include <NTPClient.h>
#include <WiFiUdp.h>

// ========== END: Imports ==========


// ========== START: Definitions ==========
#define WIFI_SSID "TEMP"
#define WIFI_PASSWORD "123456789"

#define SCOUNT 30

int twoDecimalInt;
float twoDecimal;

void connectToWiFi(char const *ssid, char const *password);

float getMedianNum(float bArray[], int iFilterLen);

// ----- Firebase Realtime Database -----
#define API_KEY "AIzaSyDmzEUgMieIOq1lqzRgbWOztIECXSuHCNs"
#define DATABASE_URL "salty-mediterranean-default-rtdb.europe-west1.firebasedatabase.app"

FirebaseData fbdo;
FirebaseAuth auth;
FirebaseConfig config;

bool signupOK = false;
int recordNum = 0;

#define mainPath "liveTesting/"

// ----- Waterproof DS18B20 -----
#define oneWireBus D4

OneWire oneWire(oneWireBus);
DallasTemperature WPTempSensor(&oneWire);

float wptempBuffer[SCOUNT];

float temperatureC = 0;

// ----- TDS Sensor -----
#define TdsSensorPin A0
#define VREF 3.3

float tdsBuffer[SCOUNT];

float averageVoltage = 0;
float tdsValue = 0;
float tdsTemperature = 25;

// ----- Ultrasonic SR04 -----
#define trigPin D5
#define echoPin D6
#define SOUND_VELOCITY 0.034
float containerRadius = 13;

float usBuffer[SCOUNT];

long duration = 0;
float initialDistanceCm = 0, distanceCm = 0;
float volume = 0;
float area = 3.14 * containerRadius * containerRadius;
unsigned long v1Time = 0;
unsigned long v2Time = 0;
float evaporationRate = 0;

// ----- DHT22 -----
#define DHTPIN D3
#define DHTTYPE DHT22

float dhtTempBuffer[SCOUNT];
float dhtHumBuffer[SCOUNT];

DHT dht(DHTPIN, DHTTYPE);
float dhtHumidity, dhtTemperature;

// ----- NTP Client -----
WiFiUDP ntpUDP;
NTPClient timeClient(ntpUDP, "pool.ntp.org");
unsigned long epochTime;

// ========== END: Definitions ==========

// ========== START: Setup ==========
void setup() {
  Serial.begin(115200);
  connectToWiFi(WIFI_SSID, WIFI_PASSWORD);

  // ----- Firebase Realtime Database -----
  config.api_key = API_KEY;
  config.database_url = DATABASE_URL;

  if (Firebase.signUp(&config, &auth, "ESP8266 NodeMCU", "")) {
    Serial.println("Signed Up to Firebase ...");
    signupOK = true;
  } else {
    Serial.println(config.signer.signupError.message.c_str());
  }

  config.token_status_callback = tokenStatusCallback;

  Firebase.begin(&config, &auth);
  Firebase.reconnectWiFi(true);

  // ----- Waterproof DS18B20 -----
  WPTempSensor.begin();

  // ----- TDS Sensor -----
  pinMode(TdsSensorPin, INPUT);

  // ----- Ultrasonic SR04 -----
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  for (byte index = 0; index < SCOUNT; index++) {
    delay(40);

    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);

    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);

    duration = pulseIn(echoPin, HIGH);
    usBuffer[index] = duration;
  }
  initialDistanceCm = getMedianNum(usBuffer, SCOUNT) * SOUND_VELOCITY / 2;
  twoDecimalInt = (int)(initialDistanceCm * 10);
  twoDecimal = twoDecimalInt / 10.0;
  initialDistanceCm = twoDecimal;
  v1Time = millis();

  // ----- DHT22 -----
  dht.begin();

  // ----- NTP Client -----
  timeClient.begin();
}
// ========== END: Setup ==========

// ========== START: Loop ==========
void loop() {
  long int execT1 = millis();

  // ========== START: Collecting data before applying Median Filtering Algorithm ==========
  for (byte index = 0; index < SCOUNT; index++) {
    delay(40);

    // ----- Waterproof DS18B20 -----
    WPTempSensor.requestTemperatures();
    wptempBuffer[index] = WPTempSensor.getTempCByIndex(0);

    // ----- TDS Sensor -----
    tdsTemperature = temperatureC;  // Change TDS temperature compensation value according to the temperature read by the Waterproof temperature sensor
    tdsBuffer[index] = analogRead(TdsSensorPin);

    // ----- Ultrasonic SR04 -----
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);

    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);

    duration = pulseIn(echoPin, HIGH);
    usBuffer[index] = duration;

    // ----- DHT22 -----
    dhtTempBuffer[index] = dht.readTemperature();
    dhtHumBuffer[index] = dht.readHumidity();

    // Check for error reading
    if (isnan(dhtHumidity) || isnan(dhtTemperature)) {
      Serial.println(" DHT reading failed ");
      return;
    }
  }
  // ========== END: Collecting data before applying Median Filtering Algorithm ==========

  // ========== START: Getting results from Median Filtering Algorithm ==========
  // ----- Waterproof DS18B20 -----
  temperatureC = getMedianNum(wptempBuffer, SCOUNT);

  // ----- TDS Sensor -----
  averageVoltage = getMedianNum(tdsBuffer, SCOUNT) * (float)VREF / 1024.0;
  float compensationCoefficient = 1.0 + 0.02 * (tdsTemperature - 25.0);
  float compensationVoltage = averageVoltage / compensationCoefficient;
  tdsValue = (133.42 * compensationVoltage * compensationVoltage * compensationVoltage - 255.86 * compensationVoltage * compensationVoltage + 857.39 * compensationVoltage) * 0.5;

  // ----- Ultrasonic SR04 -----
  distanceCm = getMedianNum(usBuffer, SCOUNT) * SOUND_VELOCITY / 2;
  twoDecimalInt = (int)(distanceCm * 10);
  twoDecimal = twoDecimalInt / 10.0;
  distanceCm = twoDecimal;
  if (distanceCm - initialDistanceCm > 0.3) {
    volume = area * (distanceCm - initialDistanceCm);
  }
  v2Time = millis();
  evaporationRate = volume / ((v2Time / 60000.0) - (v1Time / 60000.0));
  v1Time = millis();

  // ----- DHT22 -----
  dhtTemperature = getMedianNum(dhtTempBuffer, SCOUNT);
  dhtHumidity = getMedianNum(dhtHumBuffer, SCOUNT);
  // ========== END: Getting results from Median Filtering Algorithm ==========


  // ----- Firebase Realtime Database -----
  String recordNumString = String("") + recordNum;
  if (Firebase.ready() && signupOK) {
    String path = mainPath + recordNumString + "/WaterTemperature";
    // int twoDecimalInt = (int)(temperatureC * 100 + 0.5);
    // float twoDecimal = twoDecimalInt / 100.0;
    twoDecimalInt = (int)(temperatureC * 100 + 0.5);
    twoDecimal = twoDecimalInt / 100.0;

    // ----- Waterproof DS18B20 -----
    if (Firebase.RTDB.setFloat(&fbdo, path, twoDecimal)) {
      Serial.print("Passed::Water Temperature: ");
      Serial.print(twoDecimal);
      Serial.print("°C --- ");
    } else {
      Serial.println("FAILED");
      Serial.println("REASON: " + fbdo.errorReason());
    }

    // ----- TDS Sensor -----
    path = mainPath + recordNumString + "/TDS";
    twoDecimalInt = (int)(tdsValue);
    // twoDecimal = twoDecimalInt;
    if (Firebase.RTDB.setFloat(&fbdo, path, twoDecimalInt)) {
      Serial.print("Passed::TDS: ");
      Serial.print(twoDecimalInt);
      Serial.print("ppm --- ");
    } else {
      Serial.println("FAILED");
      Serial.println("REASON: " + fbdo.errorReason());
    }


    // ----- Ultrasonic SR04 -----
    
    // path = mainPath + recordNumString + "/DistanceCM";
    // // twoDecimalInt = (int)(volume * 10 + 0.5);
    // // twoDecimal = twoDecimalInt / 10.0;
    // if (Firebase.RTDB.setFloat(&fbdo, path, distanceCm)) {
    //   Serial.print("Passed:: Distance: ");
    //   Serial.print(distanceCm);
    //   Serial.print("cm --- ");
    // } else {
    //   Serial.println("FAILED");
    //   Serial.println("REASON: " + fbdo.errorReason());
    // }
    
    path = mainPath + recordNumString + "/VolumeEvaporated";
    twoDecimalInt = (int)(volume * 10 + 0.5);
    twoDecimal = twoDecimalInt / 10.0;
    if (Firebase.RTDB.setFloat(&fbdo, path, twoDecimal)) {
      Serial.print("Passed::𝚫 Volume: ");
      Serial.print(twoDecimal);
      Serial.print("cm³ --- ");
    } else {
      Serial.println("FAILED");
      Serial.println("REASON: " + fbdo.errorReason());
    }

    path = mainPath + recordNumString + "/EvaporationRate";
    twoDecimalInt = (int)(evaporationRate * 100 + 0.5);
    twoDecimal = twoDecimalInt / 100.0;
    if (Firebase.RTDB.setFloat(&fbdo, path, twoDecimal)) {
      Serial.print("Passed::Evaporation Rate: ");
      Serial.print(twoDecimal);
      Serial.print("cm³/min --- ");
    } else {
      Serial.println("FAILED");
      Serial.println("REASON: " + fbdo.errorReason());
    }

    // ----- DHT22 -----
    path = mainPath + recordNumString + "/Humidity";
    twoDecimalInt = (int)(dhtHumidity * 100 + 0.5);
    twoDecimal = twoDecimalInt / 100.0;
    if (Firebase.RTDB.setFloat(&fbdo, path, twoDecimal)) {
      Serial.print("Passed::Humidity: ");
      Serial.print(twoDecimal);
      Serial.print("% --- ");
    } else {
      Serial.println("FAILED");
      Serial.println("REASON: " + fbdo.errorReason());
    }

    // path = mainPath + recordNumString + "/AirTemperature";
    // twoDecimalInt = (int)(dhtTemperature * 100 + 0.5);
    // twoDecimal = twoDecimalInt / 100.0;
    // if (Firebase.RTDB.setFloat(&fbdo, path, twoDecimal)) {
    //   Serial.print("Passed::Air Temperature: ");
    //   Serial.print(twoDecimal);
    //   Serial.println("°C");
    // } else {
    //   Serial.println("FAILED");
    //   Serial.println("REASON: " + fbdo.errorReason());
    // }

    // ----- NTP Client -----
    timeClient.update();
    epochTime = timeClient.getEpochTime();

    path = mainPath + recordNumString + "/EpochTime";
    if (Firebase.RTDB.setInt(&fbdo, path, epochTime)) {
      Serial.print("Passed::Epoch Time: ");
      Serial.print(epochTime);
      Serial.println("sec");
    } else {
      Serial.println("FAILED");
      Serial.println("REASON: " + fbdo.errorReason());
    }

    recordNum++;
  }

  // Printing
  Serial.print("Water Temperature: ");
  Serial.print(temperatureC);
  Serial.print("°C --- ");
  Serial.print("TDS: ");
  Serial.print(tdsValue, 0);
  Serial.print("ppm --- ");
  // Serial.print("Distance: ");
  // Serial.print(distanceCm);
  // Serial.print("cm --- ");
  Serial.print("𝚫 Volume: ");
  Serial.print(volume);
  Serial.print("cm³ --- ");
  Serial.print("Evaporation Rate: ");
  Serial.print(evaporationRate);
  Serial.print("cm³/min --- ");
  Serial.print("Humidity: ");
  Serial.print(dhtHumidity);
  Serial.print("% --- ");
  // Serial.print("Air Temperature: ");
  // Serial.print(dhtTemperature);
  // Serial.println("°C");

  delay(2000);
  long int execT2 = millis();
  Serial.print("Loop execution time: ");
  Serial.print(execT2 - execT1);
  Serial.println("ms");
}
// ========== END: Loop ==========

// ========== START: connectToWiFi Function ==========
void connectToWiFi(char const *ssid, char const *password) {
  delay(10);
  Serial.println();
  Serial.print("Connecting to ");
  Serial.print(ssid);

  WiFi.mode(WIFI_STA);
  WiFi.disconnect();

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println();
  Serial.print("WiFi connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
  Serial.println();
}
// ========== END: connectToWiFi Function ==========

// ========== START: Median Filtering Algorithm (utilizing Bubble Sort Algorithm) ==========
float getMedianNum(float bArray[], int iFilterLen) {
  float bTab[iFilterLen];
  for (byte i = 0; i < iFilterLen; i++) {
    bTab[i] = bArray[i];
  }
  int i, j;
  float bTemp;
  for (j = 0; j < iFilterLen - 1; j++) {
    for (i = 0; i < iFilterLen - j - 1; i++) {
      if (bTab[i] > bTab[i + 1]) {
        bTemp = bTab[i];
        bTab[i] = bTab[i + 1];
        bTab[i + 1] = bTemp;
      }
    }
  }
  if ((iFilterLen & 1) > 0) {  // Using bitwise approach for the even/odd test
    bTemp = bTab[(iFilterLen - 1) / 2];
  } else {
    bTemp = (bTab[iFilterLen / 2] + bTab[iFilterLen / 2 - 1]) / 2;
  }
  return bTemp;
}
// ========== END: Median Filtering Algorithm (utilizing Bubble Sort Algorithm) ==========
