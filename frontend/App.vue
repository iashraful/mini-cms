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

    import * as mutationTypes from '@/store/mutations-types'
    import configMenus from '@/config/menus'

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
                    this.$bus.$emit('renderedPages', 'Navbar Updated')
                }
            },
            runForFirstTime() {
                // Currently I've plan for initial api call here.
                // Get Pages
                this.$store.dispatch('getPagesApiCall').then(() => {
                    setTimeout(() => {
                        this.updateDynamicPages();
                    }, 500)
                });
            }
        },
        created() {
            this.runForFirstTime();
        },
        mounted() {
            // Update Menus when new page added
            this.$bus.$on('addedNewPage_EB', () => {
                console.log('hello')
                this.updateDynamicPages();
            })
        }
    }
</script>
