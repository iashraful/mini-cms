import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'
// Custom Styles and JS
import './styles/base/app.main.css'

if (process.env.NODE_ENV !== 'production') {
    console.log("Running under Development....")
}

/*
import 'jquery/dist/jquery.min'
import 'popper.js/dist/popper.min'
import 'bootstrap/dist/js/bootstrap.bundle.min'
import 'bootstrap/dist/css/bootstrap.min.css'**
 */

Vue.config.productionTip = false;

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
