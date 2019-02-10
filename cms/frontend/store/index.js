import Vue from 'vue'
import Vuex from 'vuex'
import mutations from './mutations'
import actions from './actions'
import getters from './getters'
import menuItems from 'cms/frontend/config/menus'

Vue.use(Vuex);

const state = {
    appName: localStorage.getItem("appName") || 'MiNi CMS',
    appConfig: {
        app_name: '',
        footer: ''
    },
    count: 0,
    loginDetails: {},
    menus: menuItems,
    isAuthenticated: localStorage.getItem("auth") === "true",
    appLogo: "",
    token: localStorage.getItem("token") || "",
    pages: [],
    contents: [],
    routes: [],
    currentPage: {contents: []},
    searchResults: [],
};

export default new Vuex.Store({
    state,
    getters,
    actions,
    mutations,
})
