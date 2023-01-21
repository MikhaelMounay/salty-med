<template>
  <div class="container">
    <h1 class="text-center mb-4">Test Plan Results</h1>
    <p class="fs-6 text-center text-muted mb-3">
      Time since last
      <span class="fst-italic">"testPlanResults"</span> Collection update:
      <span class="fw-bold">{{
        this.lastUpdate_sec
          ? `${
              this.lastUpdate_month
                ? `${parseInt(this.lastUpdate_month)} month(s)`
                : ""
            } ${
              this.lastUpdate_day
                ? `${parseInt(this.lastUpdate_day)} day(s)`
                : ""
            } ${
              this.lastUpdate_hour
                ? `${parseInt(this.lastUpdate_hour)} hour(s)`
                : ""
            } ${
              this.lastUpdate_min
                ? `${parseInt(this.lastUpdate_min)} minute(s)`
                : ""
            } ${
              this.lastUpdate_sec
                ? `${parseInt(this.lastUpdate_sec)} second(s)`
                : ""
            }`
          : "Loading ..."
      }}</span
      >.
    </p>
    <div class="graph">
      <h4 class="text-center pt-3 mb-0">
        Graph 1: Water Temperature VS Evaporation Rate
      </h4>
      <div id="graph-1">
        <p class="fst-italic text-center pt-3">Loading ...</p>
      </div>
    </div>
    <div class="graph">
      <h4 class="text-center pt-3 mb-0">
        Graph 2: Volume of Water Evaporated VS Salinity
      </h4>
      <div id="graph-2">
        <p class="fst-italic text-center pt-3">Loading ...</p>
      </div>
    </div>
    <div class="graph">
      <h4 class="text-center pt-3 mb-0">
        Graph 3: Volume of Water Evaporated VS Relative Humidity
      </h4>
      <div id="graph-3">
        <p class="fst-italic text-center pt-3">Loading ...</p>
      </div>
    </div>
  </div>
</template>

<script>
import Plotly from "plotly.js-dist";
import firebaseApp from "../database";
import { getDatabase, ref, onValue } from "firebase/database";
import moment from "moment";
// eslint-disable-next-line
var momentDurationFormatSetup = require("moment-duration-format");

// Get Reference to "testPlanResults" Collection
const db = getDatabase(firebaseApp);
const testPlanResultsRef = ref(db, "testPlanResults");

export default {
  name: "ResultsView",
  data() {
    return {
      lastUpdate_month: 0,
      lastUpdate_day: 0,
      lastUpdate_hour: 0,
      lastUpdate_min: 0,
      lastUpdate_sec: 0,
    };
  },
  mounted() {
    onValue(testPlanResultsRef, () => {
      console.log("Firebase Update!");
      // fetch("http://127.0.0.1:5000/")
      fetch("https://salty-mediterranean.herokuapp.com/")
        .then((response) => response.text())
        .then((dataSource) => {
          if (dataSource) {
            let dataSourceParsed = JSON.parse(dataSource);
            let graph1 = document.getElementById("graph-1");
            let graph2 = document.getElementById("graph-2");
            let graph3 = document.getElementById("graph-3");

            // Graph 1 => "Water Temperature VS Evaporation Rate"
            let tempVsEvapRateJSON = JSON.parse(
              dataSourceParsed["tempVsEvapRateJSON"]
            );
            document.querySelector("#graph-1 p").style.display = "none";
            Plotly.react(
              graph1,
              tempVsEvapRateJSON.data,
              tempVsEvapRateJSON.layout,
              { responsive: true }
            );

            // Graph 2 => "Volume of Water Evaporated VS Salinity"
            let volEvapVsSalJSON = JSON.parse(
              dataSourceParsed["volEvapVsSalJSON"]
            );
            document.querySelector("#graph-2 p").style.display = "none";
            Plotly.react(
              graph2,
              volEvapVsSalJSON.data,
              volEvapVsSalJSON.layout,
              {
                responsive: true,
              }
            );

            // Graph 3 => "Volume of Water Evaporated VS Relative Humidity"
            let volEvapVsHumJSON = JSON.parse(
              dataSourceParsed["volEvapVsHumJSON"]
            );
            document.querySelector("#graph-3 p").style.display = "none";
            Plotly.react(
              graph3,
              volEvapVsHumJSON.data,
              volEvapVsHumJSON.layout,
              {
                responsive: true,
              }
            );

            // lastUpdateDuration => lastEpoch
            if (parseInt(dataSourceParsed["lastEpoch"])) {
              let lastUpdateDuration = moment
                .duration(
                  Math.round(Date.now() / 1000) -
                    parseInt(dataSourceParsed["lastEpoch"]),
                  "seconds"
                )
                .format("MM:DD:HH:mm:ss");
              this.lastUpdate_sec = lastUpdateDuration.substring(
                lastUpdateDuration.length - 2,
                lastUpdateDuration.length
              );
              this.lastUpdate_min = lastUpdateDuration.substring(
                lastUpdateDuration.length - 5,
                lastUpdateDuration.length - 3
              );
              this.lastUpdate_hour = lastUpdateDuration.substring(
                lastUpdateDuration.length - 8,
                lastUpdateDuration.length - 6
              );
              this.lastUpdate_day = lastUpdateDuration.substring(
                lastUpdateDuration.length - 11,
                lastUpdateDuration.length - 9
              );
              this.lastUpdate_month = lastUpdateDuration.substring(
                lastUpdateDuration.length - 14,
                lastUpdateDuration.length - 12
              );
            }
          } else {
            console.log("No Data Yet !!");
          }
        });
    });
  },
};
</script>

<style lang="scss" scoped>
.graph {
  min-height: 450px;
}
</style>
