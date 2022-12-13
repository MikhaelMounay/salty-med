from flask import Flask, make_response
import pandas as pd
import plotly
import plotly.express as px
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

app = Flask(__name__)
cred = credentials.Certificate("salty-mediterranean-firebase-adminsdk-2b492-3993549f39.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://salty-mediterranean-default-rtdb.europe-west1.firebasedatabase.app/"})

@app.route("/", methods=["GET"])
def index():
  ref = db.reference("/testing")
  testPlanResults = ref.get()
  if (testPlanResults != None):
    df = pd.DataFrame.from_records(testPlanResults)
    print(df)

    fig = px.line(df, x="WaterTemperature", y="TDS", title="Water Temperature VS TDS")

    fig1JSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    dictResponce = {"fig1JSON": fig1JSON, "lastEpoch": str(df.iloc[-1]["EpochTime"])}
    jsonFromDict = json.dumps(dictResponce, indent=4)
    response = make_response(jsonFromDict, 200)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
  
  else:
    response = make_response("", 200)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response



if __name__ == "__main__":
  app.run()