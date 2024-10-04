<template>
  <div class="container">
    <h1 class="text-center mb-4">Results Analysis</h1>
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

// Get Reference to "testPlanResults" Collection
const db = getDatabase(firebaseApp);
const testPlanResultsRef = ref(db, "testPlanResults");

export default {
  name: "AnalysisView",
  data() {
    return {};
  },
  mounted() {
    onValue(testPlanResultsRef, () => {
      console.log("Firebase Update!");
      //  fetch("http://127.0.0.1:5000/")
      fetch("https://salty-mediterranean.herokuapp.com/")
        .then((response) => response.text())
        .then((dataSource) => {
          if (dataSource) {
            let dataSourceParsed = JSON.parse(dataSource);
            let graph1 = document.getElementById("graph-1");
            let graph2 = document.getElementById("graph-2");
            let graph3 = document.getElementById("graph-3");

            // Graph 1 => "Water Temperature VS Evaporation Rate"
            let tempVsEvapRate_analysisJSON = JSON.parse(
              dataSourceParsed["tempVsEvapRate_analysisJSON"]
            );
            document.querySelector("#graph-1 p").style.display = "none";
            Plotly.react(
              graph1,
              tempVsEvapRate_analysisJSON.data,
              tempVsEvapRate_analysisJSON.layout,
              { responsive: true }
            );

            // Graph 2 => "Volume of Water Evaporated VS Salinity"
            let volEvapVsSal_analysisJSON = JSON.parse(
              dataSourceParsed["volEvapVsSal_analysisJSON"]
            );
            document.querySelector("#graph-2 p").style.display = "none";
            Plotly.react(
              graph2,
              volEvapVsSal_analysisJSON.data,
              volEvapVsSal_analysisJSON.layout,
              {
                responsive: true,
              }
            );

            // Graph 3 => "Volume of Water Evaporated VS Relative Humidity"
            let volEvapVsHum_analysisJSON = JSON.parse(
              dataSourceParsed["volEvapVsHum_analysisJSON"]
            );
            document.querySelector("#graph-3 p").style.display = "none";
            Plotly.react(
              graph3,
              volEvapVsHum_analysisJSON.data,
              volEvapVsHum_analysisJSON.layout,
              {
                responsive: true,
              }
            );
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
