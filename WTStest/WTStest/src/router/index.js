import Vue from "vue";
import VueRouter from "vue-router";

import Blank from "@/views/Blank.vue";
import Master_Detail from "@/views/Master_Detail.vue";
Vue.use(VueRouter);

// TODO Web Template Studio: Add routes for your new pages here.
export default new VueRouter({
  mode: "history",
  routes: [
    { path: "/Master_Detail", component: Master_Detail },
    { path: "/Blank", component: Blank },

    { path:"/", redirect: "/Blank" }
  ]
});
