from flask import Flask, make_response
import numpy as np
import pandas as pd
import plotly
import plotly.express as px
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

app = Flask(__name__)


# Initialize Firebase
cred = credentials.Certificate("salty-mediterranean-firebase-adminsdk-2b492-3993549f39.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://salty-mediterranean-default-rtdb.europe-west1.firebasedatabase.app/"})


@app.route("/", methods=["GET"])
def index():
    # Get Reference to "testPlanResults" Collection
    testPlanResultsRef = db.reference("/testPlanResults")
    testPlanResultsData = testPlanResultsRef.get()

    # Get Reference to "liveTesting" Collection
    liveTestingRef = db.reference("/liveTesting")
    liveTestingData = liveTestingRef.get()

    # Check if there is data available in the collection to work with
    if ((testPlanResultsData != None) or (liveTestingData != None)):

        # Declare pandas dataframe to hold Test Plan Results
        testPlanDf = pd.DataFrame.from_records(testPlanResultsData)

        # Declare pandas dataframe to hold Live Testing Data
        liveTestingDf = pd.DataFrame.from_records(liveTestingData)

        # Get lastEpoch time from the two collections
        lastEpoch = str(testPlanDf.iloc[-1]["EpochTime"])
        lastEpoch_live = str(liveTestingDf.iloc[-1]["EpochTime"])

        # =========================== Graphs of ResultsView in the Website ===========================

        # Graph 1 - Results => "Water Temperature VS Evaporation Rate"

        # Sort dataframe according to "WaterTemperature" values
        testPlanDf = testPlanDf.sort_values("WaterTemperature")
        # Draw scatter plot & Get JSON data of the plot
        tempVsEvapRate = px.scatter(testPlanDf, x="WaterTemperature", y="EvaporationRate", labels={"WaterTemperature": "Water Temperature (°C)", "EvaporationRate": "Evaporation Rate (mL/min)"}, color_discrete_sequence=["#e99e75"])
        tempVsEvapRate.update_layout(font=dict(family='"Inter", sans-serif'), title_x=0.5)
        tempVsEvapRateJSON = json.dumps(tempVsEvapRate, cls=plotly.utils.PlotlyJSONEncoder)

        # Graph 2 - Results => "Volume of Water Evaporated VS Salinity"

        # Sort dataframe according to "VolumeEvaporated" values
        testPlanDf = testPlanDf.sort_values("VolumeEvaporated")
        # Draw scatter plot & Get JSON data of the plot
        volEvapVsSal = px.scatter(testPlanDf, x="VolumeEvaporated", y="TDS", labels={"VolumeEvaporated": "Water Volume (mL)", "TDS": "Salinity (ppm)"}, color_discrete_sequence=["#e99e75"])
        volEvapVsSal.update_layout(font=dict(family='"Inter", sans-serif'), title_x=0.5)
        volEvapVsSalJSON = json.dumps(volEvapVsSal, cls=plotly.utils.PlotlyJSONEncoder)

        # Graph 3 - Results => "Volume of Water Evaporated VS Relative Humidity"

        # Sort dataframe according to "VolumeEvaporated" values
        testPlanDf = testPlanDf.sort_values("VolumeEvaporated")
        # Draw scatter plot & Get JSON data of the plot
        volEvapVsHum = px.scatter(testPlanDf, x="VolumeEvaporated", y="Humidity", labels={"VolumeEvaporated": "Water Volume (mL)", "TDS": "Relative Humidity (%)"}, color_discrete_sequence=["#e99e75"])
        volEvapVsHum.update_layout(font=dict(family='"Inter", sans-serif'), title_x=0.5)
        volEvapVsHumJSON = json.dumps(volEvapVsHum, cls=plotly.utils.PlotlyJSONEncoder)

        # =========================== Graphs of AnalysisView in the Website ===========================

        # Graph 1 - Analysis => "Water Temperature VS Evaporation Rate"

        # Declare new dataframe & Get 34 samples for the analysis graph
        tempVsEvapRate_analysis = pd.DataFrame({"WaterTemperature": [], "EvaporationRate": []}, dtype="float64")
        for i in range(int(len(testPlanDf.index)/10)):
            i *= 10
            tempVsEvapRate_analysis.loc[len(tempVsEvapRate_analysis.index)] = [round(testPlanDf["WaterTemperature"][i], 1), round(testPlanDf["EvaporationRate"][i], 1)]
            if (i >= len(testPlanDf.index)):
                i = len(testPlanDf.index) - 1
                tempVsEvapRate_analysis.loc[len(tempVsEvapRate_analysis.index)] = [round(testPlanDf["WaterTemperature"][i], 1), round(testPlanDf["EvaporationRate"][i], 1)]
        # Sort dataframe according to "WaterTemperature" values
        tempVsEvapRate_analysis = tempVsEvapRate_analysis.sort_values("WaterTemperature")
        # Draw scatter plot & Get JSON data of the plot
        tempVsEvapRate_analysisGraph = px.scatter(tempVsEvapRate_analysis, x="WaterTemperature", y="EvaporationRate", trendline="ols", trendline_color_override="#381902", labels={
                                                  "WaterTemperature": "Water Temperature (°C)", "EvaporationRate": "Evaporation Rate (mL/min)"}, color_discrete_sequence=["#e99e75"])
        tempVsEvapRate_analysisGraph.update_layout(font=dict(family='"Inter", sans-serif'), title_x=0.5, hovermode="x")
        tempVsEvapRate_analysisGraph.update_traces(hovertemplate=None)
        tempVsEvapRate_analysisJSON = json.dumps(tempVsEvapRate_analysisGraph, cls=plotly.utils.PlotlyJSONEncoder)
        # Get equation of regression line
        equation1 = str(np.poly1d(np.polyfit(testPlanDf["WaterTemperature"], testPlanDf["EvaporationRate"], 1)))

        # Graph 2 - Analysis => "Volume of Water Evaporated VS Salinity"

        # Declare new dataframe & Get 12 samples for the analysis graph
        volEvapVsSal_analysis = pd.DataFrame({"VolumeEvaporated": [], "TDS": []}, dtype="float64")
        for i in range(int(len(testPlanDf.index)/28)):
            i *= 28
            volEvapVsSal_analysis.loc[len(volEvapVsSal_analysis.index)] = [round(testPlanDf["VolumeEvaporated"][i], 1), round(testPlanDf["TDS"][i], 1)]
            if (i >= len(testPlanDf.index)):
                i = len(testPlanDf.index) - 1
                volEvapVsSal_analysis.loc[len(volEvapVsSal_analysis.index)] = [round(testPlanDf["VolumeEvaporated"][i], 1), round(testPlanDf["TDS"][i], 1)]
        # Sort dataframe according to "VolumeEvaporated" values
        volEvapVsSal_analysis = volEvapVsSal_analysis.sort_values("VolumeEvaporated")
        # Draw scatter plot & Get JSON data of the plot
        volEvapVsSal_analysisGraph = px.scatter(volEvapVsSal_analysis, x="VolumeEvaporated", y="TDS", trendline="ols", trendline_color_override="#381902", labels={"WaterTemperature": "Water Temperature (°C)", "EvaporationRate": "Evaporation Rate (mL/min)"}, color_discrete_sequence=["#e99e75"])
        volEvapVsSal_analysisGraph.update_layout(font=dict(family='"Inter", sans-serif'), title_x=0.5, hovermode="x")
        volEvapVsSal_analysisGraph.update_traces(hovertemplate=None)
        volEvapVsSal_analysisJSON = json.dumps(volEvapVsSal_analysisGraph, cls=plotly.utils.PlotlyJSONEncoder)
        # Get equation of regression line
        equation2 = str(np.poly1d(np.polyfit(testPlanDf["VolumeEvaporated"], testPlanDf["TDS"], 1)))

        # Graph 3 - Analysis => "Volume of Water Evaporated VS Relative Humidity"

        # Declare new dataframe & Get 12 samples for the analysis graph
        volEvapVsHum_analysis = pd.DataFrame({"VolumeEvaporated": [], "Humidity": []}, dtype="float64")
        for i in range(int(len(testPlanDf.index)/28)):
            i *= 28
            volEvapVsHum_analysis.loc[len(volEvapVsHum_analysis.index)] = [round(testPlanDf["VolumeEvaporated"][i], 1), round(testPlanDf["Humidity"][i], 1)]
            if (i >= len(testPlanDf.index)):
                i = len(testPlanDf.index) - 1
                volEvapVsHum_analysis.loc[len(volEvapVsHum_analysis.index)] = [round(testPlanDf["VolumeEvaporated"][i], 1), round(testPlanDf["Humidity"][i], 1)]
        # Sort dataframe according to "VolumeEvaporated" values
        volEvapVsHum_analysis = volEvapVsHum_analysis.sort_values("VolumeEvaporated")
        # Draw scatter plot & Get JSON data of the plot
        volEvapVsHum_analysisGraph = px.scatter(volEvapVsHum_analysis, x="VolumeEvaporated", y="Humidity", trendline="ols", trendline_color_override="#381902", labels={"VolumeEvaporated": "Water Volume (mL)", "TDS": "Relative Humidity (%)"}, color_discrete_sequence=["#e99e75"])
        volEvapVsHum_analysisGraph.update_layout(font=dict(family='"Inter", sans-serif'), title_x=0.5, hovermode="x")
        volEvapVsHum_analysisGraph.update_traces(hovertemplate=None)
        volEvapVsHum_analysisJSON = json.dumps(volEvapVsHum_analysisGraph, cls=plotly.utils.PlotlyJSONEncoder)
        # Get equation of regression line
        equation3 = str(np.poly1d(np.polyfit(testPlanDf["VolumeEvaporated"], testPlanDf["Humidity"], 1)))

        # =========================== Graphs of LiveTestingView in the Website ===========================

        # Graph 1 - LiveTesting => "Water Temperature VS Evaporation Rate"

        # Sort dataframe according to "WaterTemperature" values
        liveTestingDf = liveTestingDf.sort_values("WaterTemperature")
        # Draw scatter plot & Get JSON data of the plot
        tempVsEvapRate_live = px.scatter(liveTestingDf, x="WaterTemperature", y="EvaporationRate", labels={"WaterTemperature": "Water Temperature (°C)", "EvaporationRate": "Evaporation Rate (mL/min)"}, color_discrete_sequence=["#e99e75"])
        tempVsEvapRate_live.update_layout(font=dict(family='"Inter", sans-serif'), title_x=0.5)
        tempVsEvapRateJSON_live = json.dumps(tempVsEvapRate_live, cls=plotly.utils.PlotlyJSONEncoder)

        # Graph 2 - LiveTesting => "Volume of Water Evaporated VS Salinity"

        # Sort dataframe according to "VolumeEvaporated" values
        liveTestingDf = liveTestingDf.sort_values("VolumeEvaporated")
        # Draw scatter plot & Get JSON data of the plot
        volEvapVsSal_live = px.scatter(liveTestingDf, x="VolumeEvaporated", y="TDS", labels={"VolumeEvaporated": "Water Volume (mL)", "TDS": "Salinity (ppm)"}, color_discrete_sequence=["#e99e75"])
        volEvapVsSal_live.update_layout(font=dict(family='"Inter", sans-serif'), title_x=0.5)
        volEvapVsSalJSON_live = json.dumps(volEvapVsSal_live, cls=plotly.utils.PlotlyJSONEncoder)

        # Graph 3 - LiveTesting => "Volume of Water Evaporated VS Relative Humidity"

        # Sort dataframe according to "VolumeEvaporated" values
        liveTestingDf = liveTestingDf.sort_values("VolumeEvaporated")
        # Draw scatter plot & Get JSON data of the plot
        volEvapVsHum_live = px.scatter(liveTestingDf, x="VolumeEvaporated", y="Humidity", labels={"VolumeEvaporated": "Water Volume (mL)", "TDS": "Relative Humidity (%)"}, color_discrete_sequence=["#e99e75"])
        volEvapVsHum_live.update_layout(font=dict(family='"Inter", sans-serif'), title_x=0.5)
        volEvapVsHumJSON_live = json.dumps(volEvapVsHum_live, cls=plotly.utils.PlotlyJSONEncoder)

        # =========================== Preparing & Returning JSON response ===========================

        dictResponce = {"tempVsEvapRateJSON": tempVsEvapRateJSON, "volEvapVsSalJSON": volEvapVsSalJSON, "volEvapVsHumJSON": volEvapVsHumJSON, "tempVsEvapRate_analysisJSON": tempVsEvapRate_analysisJSON, "volEvapVsSal_analysisJSON": volEvapVsSal_analysisJSON, "volEvapVsHum_analysisJSON": volEvapVsHum_analysisJSON,
                        "equation1": equation1, "equation2": equation2, "equation3": equation3, "tempVsEvapRateJSON_live": tempVsEvapRateJSON_live, "volEvapVsSalJSON_live": volEvapVsSalJSON_live, "volEvapVsHumJSON_live": volEvapVsHumJSON_live, "lastEpoch": lastEpoch, "lastEpoch_live": lastEpoch_live}
        jsonFromDict = json.dumps(dictResponce, indent=4)
        response = make_response(jsonFromDict, 200)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    # If there is no data available in Firebase collections
    else:
        response = make_response("", 200)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response


if __name__ == "__main__":
    app.run()
