import { createRouter, createWebHashHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import AboutView from "../views/AboutView.vue";
import SystemTestingView from "../views/SystemTestingView.vue";
import ResultsView from "../views/Results.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/about",
    name: "about",
    component: AboutView,
  },
  {
    path: "/testing",
    name: "testing",
    component: SystemTestingView,
  },
  {
    path: "/results",
    name: "results",
    component: ResultsView,
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
