<template>
    <div id="app">
        <div v-if="loading" class="text-center mx-auto mt-5">
            <img src="/static/img/loading.gif" width="150"/>
        </div>
        <div v-if="!loading">
            <top-nav-bar/>
            <side-nav-bar v-if="isAuth"/>
            <app-content>
                <router-view slot="main-content"/>
                <app-footer slot="main-content"/>
            </app-content>
        </div>
    </div>
</template>

<script>
    import TopNavBar from './components/navbars/TopNavBar'
    import SideNavBar from './components/navbars/SideNavBar'
    import AppContent from "components/utils/common/AppContent";
    import PublicContent from "components/utils/common/PublicContent";
    import Login from "components/authentications/Login";
    import AppFooter from "components/navbars/Footer";
    import PageDetails from "components/pages/PageDetails";

    import * as mutationTypes from 'store/mutations-types'
    import configMenus from 'config/menus'

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
                isAuth: this.$store.state.isAuthenticated,
                loading: true,
            }
        },
        methods: {
            updateDynamicPages() {
                const pages = this.$store.state.pages;
                let menuItems = [];
                for (let i = 0; i < pages.length; i++) {
                    menuItems.push({
                        name: pages[i].name,
                        path: '/p/' + pages[i].path,
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
                    let mergedMenus = configMenus.concat(menuItems);
                    this.$store.commit(mutationTypes.updateMenuItems, mergedMenus);
                    this.$bus.$emit('EB_RenderedPages', 'Navbar Updated')
                }
            },
            runForFirstTime() {
                // Currently I've plan for initial api call here.
                // Get Pages
                this.$store.dispatch('getAppConfigFromApi').then(() => {

                });
                this.$store.dispatch('getPagesApiCall').then(() => {
                    setTimeout(() => {
                        this.updateDynamicPages();
                        this.loading = false;
                    }, 500)
                });
            }
        },
        created() {
            this.runForFirstTime();
            // Loading off
            this.$bus.$on('EB_RenderedPages', () => {
                this.loading = false;
            })
        },
        mounted() {
            // Update Menus when new page added
            this.$bus.$on('EB_PageChanged', () => {
                this.updateDynamicPages();
            })
        }
    }
</script>
