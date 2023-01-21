<template>
  <div class="container pb-5">
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
    <div class="prediction row g-5">
      <div class="col-lg-6 col-12">
        <label for="water-temp" class="form-label"
          >Enter Water Temperature
          <span class="text-small text-muted">(°C)</span>:
        </label>
        <div class="row gx-5">
          <div class="col-8">
            <input
              type="number"
              class="form-control"
              v-model="equation1_input"
              placeholder="0"
              @keyup.enter="calcEquation(1)"
            />
          </div>
          <div class="col">
            <input
              type="submit"
              value="Calculate"
              class="btn btn-primary"
              @click="calcEquation(1)"
              @keyup.enter="calcEquation(1)"
            />
          </div>
        </div>
      </div>
      <div class="col-lg-6 col-12">
        <label for="water-temp" class="form-label"
          >Evaporation Rate <span class="text-small text-muted">(mL/min)</span>:
        </label>
        <input
          type="text"
          class="form-control-plaintext"
          readonly
          v-model="equation1_result"
        />
      </div>
    </div>
    <hr />
    <div class="graph">
      <h4 class="text-center pt-3 mb-0">
        Graph 2: Volume of Water Evaporated VS Salinity
      </h4>
      <div id="graph-2">
        <p class="fst-italic text-center pt-3">Loading ...</p>
      </div>
    </div>
    <div class="prediction row g-5">
      <div class="col-lg-6 col-12">
        <label for="water-temp" class="form-label"
          >Enter Volume of Water Evaporated
          <span class="text-small text-muted">(mL)</span>:
        </label>
        <div class="row gx-5">
          <div class="col-8">
            <input
              type="number"
              class="form-control"
              v-model="equation2_input"
              placeholder="0"
              @keyup.enter="calcEquation(2)"
            />
          </div>
          <div class="col">
            <input
              type="submit"
              value="Calculate"
              class="btn btn-primary"
              @click="calcEquation(2)"
              @keyup.enter="calcEquation(2)"
            />
          </div>
        </div>
      </div>
      <div class="col-lg-6 col-12">
        <label for="water-temp" class="form-label"
          >Salinity <span class="text-small text-muted">(ppm)</span>:
        </label>
        <input
          type="text"
          class="form-control-plaintext"
          readonly
          v-model="equation2_result"
        />
      </div>
    </div>
    <hr />
    <div class="graph">
      <h4 class="text-center pt-3 mb-0">
        Graph 3: Volume of Water Evaporated VS Relative Humidity
      </h4>
      <div id="graph-3">
        <p class="fst-italic text-center pt-3">Loading ...</p>
      </div>
    </div>
    <div class="prediction row g-5">
      <div class="col-lg-6 col-12">
        <label for="water-temp" class="form-label"
          >Enter Volume of Water Evaporated
          <span class="text-small text-muted">(mL)</span>:
        </label>
        <div class="row gx-5">
          <div class="col-8">
            <input
              type="number"
              class="form-control"
              v-model="equation3_input"
              placeholder="0"
              @keyup.enter="calcEquation(3)"
            />
          </div>
          <div class="col">
            <input
              type="submit"
              value="Calculate"
              class="btn btn-primary"
              @click="calcEquation(3)"
              @keyup.enter="calcEquation(3)"
            />
          </div>
        </div>
      </div>
      <div class="col-lg-6 col-12">
        <label for="water-temp" class="form-label"
          >Relative Humidity <span class="text-small text-muted">(%)</span>:
        </label>
        <input
          type="text"
          class="form-control-plaintext"
          readonly
          v-model="equation3_result"
        />
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

// Get Reference to "liveTesting" Collection
const db = getDatabase(firebaseApp);
const liveTestingRef = ref(db, "liveTesting");

export default {
  name: "ResultsView",
  data() {
    return {
      lastUpdate_month: 0,
      lastUpdate_day: 0,
      lastUpdate_hour: 0,
      lastUpdate_min: 0,
      lastUpdate_sec: 0,
      equation1: "",
      equation2: "",
      equation3: "",
      equation1_input: null,
      equation2_input: null,
      equation3_input: null,
      equation1_result: 0,
      equation2_result: 0,
      equation3_result: 0,
    };
  },
  methods: {
    calcEquation(equationNumber) {
      let result = 0;
      switch (equationNumber) {
        case 1:
          result = eval(
            this.equation1.replaceAll("x", `* ${this.equation1_input}`)
          );
          this.equation1_result = result >= 0 ? result : 0;
          break;
        case 2:
          result = eval(
            this.equation2.replaceAll("x", `* ${this.equation2_input}`)
          );
          this.equation2_result = result >= 0 ? result : 0;
          break;
        case 3:
          result = eval(
            this.equation3.replaceAll("x", `* ${this.equation3_input}`)
          );
          this.equation3_result = result >= 0 ? result : 0;
          break;
      }
    },
  },
  mounted() {
    onValue(liveTestingRef, () => {
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
            let tempVsEvapRateJSON_live = JSON.parse(
              dataSourceParsed["tempVsEvapRateJSON_live"]
            );
            document.querySelector("#graph-1 p").style.display = "none";
            Plotly.react(
              graph1,
              tempVsEvapRateJSON_live.data,
              tempVsEvapRateJSON_live.layout,
              { responsive: true }
            );

            // Graph 2 => "Volume of Water Evaporated VS Salinity"
            let volEvapVsSalJSON_live = JSON.parse(
              dataSourceParsed["volEvapVsSalJSON_live"]
            );
            document.querySelector("#graph-2 p").style.display = "none";
            Plotly.react(
              graph2,
              volEvapVsSalJSON_live.data,
              volEvapVsSalJSON_live.layout,
              {
                responsive: true,
              }
            );

            // Graph 3 => "Volume of Water Evaporated VS Relative Humidity"
            let volEvapVsHumJSON_live = JSON.parse(
              dataSourceParsed["volEvapVsHumJSON_live"]
            );
            document.querySelector("#graph-3 p").style.display = "none";
            Plotly.react(
              graph3,
              volEvapVsHumJSON_live.data,
              volEvapVsHumJSON_live.layout,
              {
                responsive: true,
              }
            );

            // Get equations of the line of regressions
            this.equation1 = dataSourceParsed["equation1"];
            this.equation2 = dataSourceParsed["equation2"];
            this.equation3 = dataSourceParsed["equation3"];

            // lastUpdateDuration => lastEpoch_live
            if (parseInt(dataSourceParsed["lastEpoch_live"])) {
              let lastUpdateDuration = moment
                .duration(
                  Math.round(Date.now() / 1000) -
                    parseInt(dataSourceParsed["lastEpoch_live"]),
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
@import "../assets/scss/_variables";

input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

input[type="number"] {
  -moz-appearance: textfield;
}

.graph {
  min-height: 550px;
}

.prediction {
  & > div {
    border-radius: 3px;
    padding-top: 1rem;
    padding-bottom: 1.5rem;
    &:nth-child(1) {
      border-left: 4px solid $boxColor;
    }
    .form-control {
      background-color: #eee;
      &:focus {
        background-color: #fff;
        border-color: $main-color;
        box-shadow: 0 0 0 0.25rem
          transparentize($color: $main-color, $amount: 0.25);
      }
    }
    .form-control-plaintext {
      background-color: #eee;
      border-radius: 0.375rem;
      padding: 0.375rem 0.75rem;
    }
    .btn {
      background-color: $main-color;
      border-color: $main-color;
      &:focus {
        border-color: $main-color;
        box-shadow: 0 0 0 0.25rem
          transparentize($color: $main-color, $amount: 0.25);
      }
    }
  }
}

hr {
  margin-bottom: 1.5rem;
}
</style>
