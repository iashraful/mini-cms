<template>
    <div>
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <a class="navbar-brand" href="/#/">{{ appName }}</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarColor02"
                    aria-controls="navbarColor02" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarColor02">
                <ul class="navbar-nav ml-auto">
                    <li class="nav-item active" v-for="item in navItems">
                        <router-link class="nav-link" v-bind:to="item.path"> {{ item.name }}</router-link>
                    </li>
                </ul>
                <ul class="navbar-nav ml-auto" v-if="isAuth">
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button"
                           data-toggle="dropdown"
                           aria-haspopup="true" aria-expanded="false">
                            <img src="/static/img/no-user-image.png" width="25" class="rounded-circle"/>
                        </a>
                        <div class="dropdown-menu dropdown-menu-right" aria-labelledby="navbarDropdown">
                            <router-link class="dropdown-item" to="/me">Profile</router-link>
                            <router-link class="dropdown-item" to="/settings">Settings</router-link>
                            <router-link class="dropdown-item" to="/logout">Logout</router-link>
                        </div>
                    </li>
                </ul>
            </div>
        </nav>
    </div>
</template>

<script>
    import * as mutationTypes from 'cms/frontend/store/mutations-types'
    import store from 'cms/frontend/store'
    import axios from 'axios'

    export default {
        name: "top-nav-bar",
        data() {
            return {
                appName: this.$store.state.appConfig.app_name,
                isAuth: this.$store.state.isAuthenticated,
                topNavLogo: store.state.appLogo,
                navItems: [],
                dropdownItems: [],
                loggedInUser: 'Test User',
                searchLoading: true,
            }
        },
        methods: {
            getLogo() {
                const url = "/api/app-logo/";
                const payload = {
                    'headers': {
                        'Content-Type': 'application/json',
                        'Authorization': 'Token ' + store.state.token
                    }
                };
                axios.get(url, payload).then((response) => {
                    store.commit(mutationTypes.updateLogo, response.data)
                    this.topNavLogo = response.data.logo;
                }).catch((err) => {
                    console.log(err)
                })
            },
            menuManager() {
                this.dropdownItems = [];
                this.navItems = [];
                for (let i = 0; i < this.$store.state.menus.length; i++) {
                    const menus = this.$store.state.menus;
                    if (menus[i].is_dropdown) {
                        this.dropdownItems.push({
                            path: menus[i].path,
                            name: menus[i].name
                        })
                    }
                    if (!menus[i].is_hidden && menus[i].is_main_menu) {
                        this.navItems.push({
                            path: menus[i].path,
                            name: menus[i].name
                        })
                    }
                }
            },
        },
        created() {
            /**
             * Here I'll parse the name and path of each route.
             * This method will trigger when vue component instance will created.
             */
            // Generate menu
            this.menuManager();
            this.$bus.$on('EB_RenderedPages', () => {
                this.menuManager();
            });
            this.$bus.$on('EB_ConfigUpdated', () => {
                this.appName = this.$store.state.appConfig.app_name;
            });
        }
    }
</script>

<style scoped>
    .navbar {
        padding: 0 5rem 0 5rem !important;
    }
</style>
