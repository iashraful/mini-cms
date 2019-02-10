import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'
import EventBus from '@/config/event-bus'
import Buefy from 'buefy'
import VueSuperCallMethod from 'vue-super-call'

if (process.env.NODE_ENV !== 'production') {
    console.log("Running under Development....")
}

Vue.use(Buefy)
Vue.config.productionTip = false;
Vue.prototype.$super = VueSuperCallMethod;
Vue.prototype.$bus = EventBus;

router.beforeEach((to, from, next) => {
    if (!to.matched.length) {
        next('/404');
    } else {
        next();
    }
});


/* eslint-disable no-new */
new Vue({
    el: '#app',
    router,
    store,
    components: {App},
    template: '<App/>'
});
