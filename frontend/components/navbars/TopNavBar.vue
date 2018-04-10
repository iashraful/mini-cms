<template>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <a class="navbar-brand" href="/#/">MiNi CMS</a>
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
            <ul class="navbar-nav ml-auto">
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button"
                       data-toggle="dropdown"
                       aria-haspopup="true" aria-expanded="false">
                        Dropdown
                    </a>
                    <div class="dropdown-menu dropdown-menu-right" aria-labelledby="navbarDropdown">
                        <a class="dropdown-item" href="#">Action</a>
                        <a class="dropdown-item" href="#">Another action</a>
                        <div class="dropdown-divider"></div>
                        <a class="dropdown-item" href="#">Something else here</a>
                    </div>
                </li>
            </ul>
        </div>
    </nav>
</template>

<script>
    import menuStore from '@/store/menu-store/menu-store'
    import * as mutationTypes from '@/store/mutations-types'
    import store from '@/store/index'
    import axios from 'axios'

    export default {
        name: "top-nav-bar",
        data() {
            return {
                searchQuery: "",
                topNavLogo: store.state.appLogo,
                navItems: [],
                dropdownItems: []
            }
        },
        methods: {
            toggleNavbar() {
                let x = document.getElementById("myTopnav");
                let s = document.getElementById("top-nav-search");
                if (x.className === "topnav") {
                    x.className += " responsive";
                } else {
                    x.className = "topnav";
                }
                if (s.className === "search-area") {
                    s.className += " responsive";
                } else {
                    s.className = "search-area";
                }
            },
            searchSubmit() {
                console.log(this.searchQuery)
            },
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
            }
        },
        created() {
            /**
             * Here I'll parse the name and path of each route.
             * This method will trigger when vue component instance will created.
             */
            // Get logo of the app
            if (store.state.isAuthenticated) {
                this.getLogo();
            }
            for (let i = 0; i < menuStore.state.menu.length; i++) {
                const menus = menuStore.state.menu;
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
        mounted() {
            // console.log(this.navItems);
        }
    }
</script>

<style scoped>
    .navbar {
        padding: 0 10px 0 10px !important;
    }
</style>
