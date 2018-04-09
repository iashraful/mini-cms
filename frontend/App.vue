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
    import store from '@/store/index.js'
    import TopNavBar from './components/navbars/TopNavBar'
    import SideNavBar from './components/navbars/SideNavBar'
    import AppContent from "@/components/utils/common/AppContent";
    import PublicContent from "@/components/utils/common/PublicContent";
    import Login from "@/components/authentications/Login";
    import AppFooter from "@/components/navbars/Footer";

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
                isAuth: store.state.isAuthenticated
            }
        }
    }
</script>
