import Vue from 'vue'
import Router from 'vue-router'

import store from '@/store/index'

Vue.use(Router);

let routes = [];
for (let i = 0; i < store.state.menus.length; i++) {
    const menus = store.state.menus;
    let route = {
        path: menus[i].path,
        name: menus[i].name,
        component: menus[i].component,
    };
    let subMenuTemp = [];
    if (menus[i].submenus.length > 0) {
        const subMenus = menus[i].submenus;
        for (let s = 0; s < subMenus.length; s++) {
            subMenuTemp.push({
                path: subMenus[s].path,
                component: subMenus[s].component,
                // Pass meta property when it has and only has child routes
                meta: {parentRouteName: route.name}
            })
        }
        // Remove default name from route
        delete route.name;
        // Extra route for redirection
        subMenuTemp.push({
            path: '/',
            redirect: subMenus[0].path
        });
    }
    if (subMenuTemp.length > 0) {
        route['children'] = subMenuTemp;
    }
    routes.push(route);
}

export default new Router({
    // mode: 'history',
    routes: routes
})
