import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import "bootstrap/dist/js/bootstrap.min.js";
import "bootstrap/dist/css/bootstrap.min.css";
import { MotionPlugin } from "@vueuse/motion";
import "animate.css";
// import { initializeApp } from "firebase/app";
// import { getDatabase } from "firebase/database";

// const firebaseConfig = {
//   apiKey: "AIzaSyDmzEUgMieIOq1lqzRgbWOztIECXSuHCNs",
//   authDomain: "salty-mediterranean.firebaseapp.com",
//   databaseURL:
//     "https://salty-mediterranean-default-rtdb.europe-west1.firebasedatabase.app",
//   projectId: "salty-mediterranean",
//   storageBucket: "salty-mediterranean.appspot.com",
//   messagingSenderId: "1013315367632",
//   appId: "1:1013315367632:web:3c46078864e93a2e7424d5",
//   measurementId: "G-92VYY9C3PW",
// };

// // eslint-disable-next-line no-unused-vars
// const firebaseApp = initializeApp(firebaseConfig);

createApp(App).use(router).use(MotionPlugin).mount("#app");
