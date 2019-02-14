<template>
    <div>
        <nav class="navbar is-dark" role="navigation" aria-label="main navigation">
            <div class="navbar-brand">
                <a role="button" class="navbar-burger burger" aria-label="menu" aria-expanded="false"
                   data-target="cmsTopNavbar">
                    <span aria-hidden="true"></span>
                    <span aria-hidden="true"></span>
                    <span aria-hidden="true"></span>
                </a>
            </div>

            <div id="cmsTopNavbar" class="navbar-menu">
                <div class="navbar-start">
                    <router-link
                            class="navbar-item"
                            to="/">
                        Home
                    </router-link>
                </div>
            </div>
        </nav>
    </div>
</template>

<script>
    export default {
        name: 'top-nav-bar',
        data () {
            return {
                appName: this.$store.state.appConfig.app_name,
                isAuth: this.$store.state.isAuthenticated
            }
        }
    }
</script>

<style scoped>
    .navbar {
        padding: 0 5rem 0 5rem !important;
    }
</style>
