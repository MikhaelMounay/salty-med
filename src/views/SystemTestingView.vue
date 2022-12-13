<template>
  <div>
    <h1 class="text-center mb-5">Testing The System</h1>
    <!-- <div id="plot-container"> -->
    <p class="fs-5">
      Time since last DB update
      <span class="fw-bold">{{ lastUpdateDuration || "Loading ..." }}</span>
      seconds.
    </p>
    <div id="myPlot">
      <p class="fst-italic text-center">Loading ...</p>
    </div>
    <!-- </div> -->
  </div>
</template>

<script>
import Plotly from "plotly.js-dist";
import firebaseApp from "../database";
import { getDatabase, ref, onValue } from "firebase/database";

const db = getDatabase(firebaseApp);
const testingRef = ref(db, "testing");

// import database from "../database";

// const testingDB = database.ref("/testing");

export default {
  name: "SystemTestingView",
  data() {
    return {
      lastUpdateDuration: 0,
    };
  },
  mounted() {
    let myPlot = document.getElementById("myPlot");

    // fetch("http://127.0.0.1:5000/")
    //   .then((response) => response.text())
    //   .then((dataSource) => {
    //     let fig = JSON.parse(dataSource);
    //     fig["data"]["0"]["line"]["color"] = "#e99e75";
    //     console.log(fig);
    //     document.querySelector("#myPlot p").style.display = "none";
    //     Plotly.newPlot(myPlot, fig.data, fig.layout, { responsive: true });
    //   });

    // document.addEventListener("asideToggled", () => {
    //   setTimeout(() => {
    //     Plotly.relayout(myPlot, {
    //       width: document.getElementById("measure").clientWidth,
    //       height: document.getElementById("plot-container").clientHeight,
    //     });
    //   }, 300);
    // });

    // testingDB.onWrite(() => {
    //   fetch("http://127.0.0.1:5000/")
    //     .then((response) => response.text())
    //     .then((dataSource) => {
    //       let fig = JSON.parse(dataSource);
    //       fig["data"]["0"]["line"]["color"] = "#e99e75";
    //       console.log(fig);
    //       document.querySelector("#myPlot p").style.display = "none";
    //       Plotly.newPlot(myPlot, fig.data, fig.layout, { responsive: true });
    //     });
    // });

    onValue(testingRef, () => {
      // const data = snapshot.val();
      console.log("value changed");
      // fetch("http://127.0.0.1:5000/")
      fetch("https://salty-mediterranean.herokuapp.com/")
        .then((response) => response.text())
        .then((dataSource) => {
          if (dataSource) {
            let dataSourceParsed = JSON.parse(dataSource);
            let fig = JSON.parse(dataSourceParsed["fig1JSON"]);
            fig["data"]["0"]["line"]["color"] = "#e99e75";
            console.log(fig);
            // console.log(parseInt(dataSourceParsed["lastEpoch"]));
            document.querySelector("#myPlot p").style.display = "none";
            Plotly.react(myPlot, fig.data, fig.layout, { responsive: true });
            if (parseInt(dataSourceParsed["lastEpoch"])) {
              console.log(Math.round(Date.now() / 1000));
              console.log(parseInt(dataSourceParsed["lastEpoch"]));
              this.lastUpdateDuration =
                Math.round(Date.now() / 1000) -
                parseInt(dataSourceParsed["lastEpoch"]);
              console.log(this.lastUpdateDuration);
            }
          } else {
            console.log("No Data Yet !!");
          }
        });
    });
  },
};
</script>

<style lang="scss" scoped></style>
