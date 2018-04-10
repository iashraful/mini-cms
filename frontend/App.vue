<template>
    <div id="app">
        <top-nav-bar/>
        <side-nav-bar v-if="isAuth"/>
        <app-content>
            <router-view slot="main-content"/>
            <app-footer slot="main-content"/>
        </app-content>
    </div>
</template>

<script>
    import TopNavBar from './components/navbars/TopNavBar'
    import SideNavBar from './components/navbars/SideNavBar'
    import AppContent from "@/components/utils/common/AppContent";
    import PublicContent from "@/components/utils/common/PublicContent";
    import Login from "@/components/authentications/Login";
    import AppFooter from "@/components/navbars/Footer";
    import PageDetails from "@/components/settings/pages/PageDetails";
    import router from '@/router/index'

    import * as mutationTypes from '@/store/mutations-types'

    export default {
        name: 'app',
        components: {
            AppFooter,
            Login,
            PublicContent,
            AppContent,
            TopNavBar,
            SideNavBar
        },
        data() {
            return {
                isAuth: this.$store.state.isAuthenticated
            }
        },
        methods: {
            updateDynamicPages() {
                const pages = this.$store.state.pages;
                let menuItems = [];
                for (let i = 0; i < pages.length; i++) {
                    menuItems.push({
                        name: pages[i].name,
                        path: '/' + pages[i].path,
                        identifier: 'app-' + pages[i].path,
                        component: PageDetails,
                        submenus: [],
                        dropdown_items: [],
                        is_dropdown: false,
                        is_hidden: false,
                        is_main_menu: true,
                        auth: true
                    })
                }
                if (menuItems.length > 0) {
                    this.$store.commit(mutationTypes.updateMenuItems, menuItems);
                    this.$bus.$emit('renderedPages', 'Navbar Updated')
                }
            },
            updateRouterWithPages() {
                let routes = router.options.routes;
                const pages = this.$store.state.menus;
                for (let i = 0; i < pages.length; i++) {
                    const menus = pages;
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
                if (routes.length > 0) {
                    this.$store.commit(mutationTypes.updateRoutes, routes);
                }
            }
        },
        created() {
            // Currently I've plan for initial api call here.
            // Get Pages
            this.$store.dispatch('getPagesApiCall').then(() => {
                setTimeout(() => {
                    this.updateDynamicPages();
                    this.updateRouterWithPages();
                }, 500)
            });


        }
    }
</script>
