import Vue from 'vue'
import Vuex from 'vuex'
import menuItems from '../../config/menus'
import mutations from './mutations'

Vue.use(Vuex);

const state = {
    menu: menuItems
};

export default new Vuex.Store({
    state,
    mutations
})