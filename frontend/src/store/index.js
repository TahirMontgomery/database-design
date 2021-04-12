import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    user: {
      isLoggedIn: null,
      uid: null,
      firstName: null,
      role: null,
    },
  },
  mutations: {
    login(state, payload) {
      // payload => {uid: Int, isLoggedIn: True, firstName: String}
      state.user = payload;
    },
    logout(state) {
      state.user = {
        sLoggedIn: null,
        uid: null,
        firstName: null,
        role: null,
      };
    },
  },
  actions: {},
  modules: {},
});
