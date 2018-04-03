import * as mutationTypes from './mutations-types'

export default {
    [mutationTypes.increment](state) {
        state.count++
    },

    [mutationTypes.login](state, {loginData}) {
        state.loginDetails = loginData;
    },

    [mutationTypes.updateLogo](state, payload) {
        state.appLogo = payload.logo;
    },
}
