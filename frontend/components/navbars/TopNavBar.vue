<template>
    <div>
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <a class="navbar-brand" href="/#/">{{ appName }}</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarColor02"
                    aria-controls="navbarColor02" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarColor02">
                <ul class="navbar-nav mr-auto">
                    <li class="nav-item active" v-for="item in navItems">
                        <router-link class="nav-link" v-bind:to="item.path"> {{ item.name }}</router-link>
                    </li>
                </ul>
                <ul class="navbar-nav ml-auto" v-if="!isAuth">
                    <li class="nav-item">
                        <form class="form-inline" v-on:submit.prevent="handleSearchSubmit">
                            <input v-model="searchQuery"
                                   class="form-control mr-sm-2"
                                   type="search" aria-label="Search"
                                   placeholder="Search"
                            />
                        </form>
                    </li>
                    <li class="nav-item active">
                        <router-link class="nav-link" to="/login">Login</router-link>
                    </li>
                </ul>
                <ul class="navbar-nav ml-auto" v-if="isAuth">
                    <li class="nav-item" style="margin-top: 2px;">
                        <form class="form-inline">
                            <input v-model="searchQuery"
                                   class="form-control mr-sm-2"
                                   type="search" aria-label="Search"
                                   placeholder="Search"
                            />
                        </form>
                    </li>
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
        <div class="search-wrapper" v-if="searchQuery.length > 0">
            <h3 class="text-center" v-if="searchLoading">Loading...</h3>
            <div>
                <ul v-for="item in searchResults">
                    <li>{{ item.title }}</li>
                </ul>
                <p class="text-center" v-if="searchResults.length <= 0 && !searchLoading">Nothing found.</p>
            </div>
        </div>
    </div>
</template>

<script>
    import * as mutationTypes from '@/store/mutations-types'
    import store from '@/store/index'
    import axios from 'axios'

    export default {
        name: "top-nav-bar",
        data() {
            return {
                searchQuery: "",
                appName: this.$store.state.appConfig.app_name,
                isAuth: this.$store.state.isAuthenticated,
                topNavLogo: store.state.appLogo,
                navItems: [],
                dropdownItems: [],
                loggedInUser: 'Test User',
                searchLoading: true,
                searchResults: [],
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
            handleSearchSubmit() {
                // console.log(this.searchQuery)
            }
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
        },
        watch: {
            searchQuery(newVal) {
                this.searchResults = [];
                this.searchLoading = true;
                this.$store.dispatch('getSearchResults', newVal).then((response) => {
                    this.searchResults = response;
                    this.searchLoading = false;
                })
            }
        }
    }
</script>

<style scoped>
    .navbar {
        padding: 0 10px 0 10px !important;
    }

    .search-wrapper {
        display: block;
        min-width: 360px;
        z-index: 2;
        position: absolute;
        background-color: #f2ebf3;
        right: 4.5rem;
        padding: .5rem 1.5rem;
    }
</style>
