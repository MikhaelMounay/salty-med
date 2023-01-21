import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import "bootstrap/dist/js/bootstrap.min.js";
import "bootstrap/dist/css/bootstrap.min.css";
import { MotionPlugin } from "@vueuse/motion";
import "animate.css";

createApp(App).use(router).use(MotionPlugin).mount("#app");
