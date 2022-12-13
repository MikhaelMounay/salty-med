import { createRouter, createWebHashHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import AboutView from "../views/AboutView.vue";
import SystemTestingView from "../views/SystemTestingView.vue";

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
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;