import { createRouter, createWebHashHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import AboutView from "../views/AboutView.vue";
import LiveTestingView from "../views/LiveTestingView.vue";
import ResultsView from "../views/ResultsView.vue";
import AnalysisView from "../views/AnalysisView.vue";
import RealDataView from "../views/RealDataView.vue";

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
    component: LiveTestingView,
  },
  {
    path: "/results",
    name: "results",
    component: ResultsView,
  },
  {
    path: "/analysis",
    name: "analysis",
    component: AnalysisView,
  },
  {
    path: "/data",
    name: "data",
    component: RealDataView,
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition;
    } else {
      return { top: 0 };
    }
  },
});

export default router;
