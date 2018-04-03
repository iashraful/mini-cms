<template src="../../templates/navbars/top-nav-bar.html"></template>

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
                if(menus[i].is_dropdown) {
                    this.dropdownItems.push({
                        path: menus[i].path,
                        name: menus[i].name
                    })
                }
                if(!menus[i].is_hidden && menus[i].is_main_menu && menus[i].auth) {
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

<style scoped src="../../styles/navbars/top-nav-bar.css"></style>
