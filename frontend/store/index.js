import Vue from 'vue'
import Vuex from 'vuex'
import mutations from './mutations'

Vue.use(Vuex);

const state = {
    count: 0,
    loginDetails: {},
    isAuthenticated: localStorage.getItem("auth") === "true",
    appLogo: "",
    token: localStorage.getItem("token") || "",
};

export default new Vuex.Store({
    state,
    mutations,
})
