import "@fortawesome/fontawesome-free/css/all.min.css";
import "bootstrap-css-only/css/bootstrap.min.css";
import "mdbvue/lib/css/mdb.min.css";
import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import faker from "faker";
import * as mdbvue from "mdbvue";
for (const component in mdbvue) {
  Vue.component(component, mdbvue[component]);
}

import VueSidebarMenu from "vue-sidebar-menu";
import "vue-sidebar-menu/dist/vue-sidebar-menu.css";
Vue.use(VueSidebarMenu);

Vue.config.productionTip = false;
Vue.prototype.faker = faker;

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
