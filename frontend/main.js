import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'
import EventBus from '@/config/event-bus'
// Custom Styles and JS
import './styles/base/app.main.css'
import './styles/rich-text-editor/quill-custom.css'

if (process.env.NODE_ENV !== 'production') {
    console.log("Running under Development....")
}

Vue.config.productionTip = false;
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
