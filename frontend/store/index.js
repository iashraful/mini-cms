import Vue from 'vue'
import Vuex from 'vuex'
import mutations from './mutations'
import actions from './actions'
import getters from './getters'
import menuItems from '@/config/menus'

Vue.use(Vuex);

const state = {
    appName: localStorage.getItem("appName") || 'MiNi CMS',
    count: 0,
    loginDetails: {},
    menus: menuItems,
    isAuthenticated: localStorage.getItem("auth") === "true",
    appLogo: "",
    token: localStorage.getItem("token") || "",
    pages: [],
    contents: [],
    routes: [],
    currentPage: {},
};

export default new Vuex.Store({
    state,
    getters,
    actions,
    mutations,
})
