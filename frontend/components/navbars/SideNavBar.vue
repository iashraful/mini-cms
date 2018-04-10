<template>
    <div class="sidenav">
        <router-link v-for="item in navItems" v-bind:to="item.path">{{ item.name }}</router-link>
    </div>
</template>

<script>
    export default {
        name: "side-nav-bar",
        data() {
            return {
                navItems: [],
                dropdownItems: []
            }
        },
        mounted() {
            const currentRouteName = this.$route.meta.parentRouteName;
            this.updateChildRoutes(currentRouteName)
        },
        methods: {
            updateChildRoutes(currentRouteName) {
                for (let i = 0; i < this.$store.state.menus.length; i++) {
                    const menus = this.$store.state.menus;
                    if (menus[i].submenus.length > 0) {
                        const parentPath = menus[i].path;
                        if (menus[i].name === currentRouteName) {
                            const subMenus = menus[i].submenus;
                            for (let s = 0; s < subMenus.length; s++) {
                                if (subMenus[s].is_dropdown) {
                                    this.dropdownItems.push({
                                        path: parentPath + '/' + subMenus[s].path,
                                        name: subMenus[s].name
                                    })
                                }
                                if (!subMenus[s].is_hidden && !subMenus[s].is_main_menu) {
                                    this.navItems.push({
                                        path: parentPath + '/' + subMenus[s].path,
                                        name: subMenus[s].name
                                    })
                                }
                            }
                            break
                        }
                    }
                    else {
                        this.navItems = [];
                        // this.dropdown_items = [];
                    }
                }
            }
        },
        watch: {
            '$route'(to, from) {
                let currentRouteName = to.meta.parentRouteName;
                this.updateChildRoutes(currentRouteName)
            }
        }
    }
</script>

<style scoped src="../../styles/navbars/side-nav-bar.css"></style>