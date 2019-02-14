import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'

Vue.use(Router);

let routes = [
    {
        name: 'home',
        path: '/',
        component: Home
    }
];

export default new Router({
    // mode: 'history',
    routes: routes
})
