<template>
    <div class="app-menu-sync">
        <button class="btn btn-primary" v-on:click="syncMenu">Sync Menu</button>
    </div>
</template>

<script>
    import * as mutationTypes from '@/store/mutations-types'

    export default {
        name: "sync-menu",
        methods: {
            syncMenu() {
                console.log("Syncing Menu Items...");
                const menus = this.$store.state.menus;
                let menuGroup = [];
                for (let i = 0; i < menus.length; i++) {
                    let eachMenu = {
                        path: menus[i].path,
                        identifier: menus[i].identifier,
                        name: menus[i].name,
                        auth: menus[i].auth,
                        is_dropdown: menus[i].is_dropdown,
                        is_hidden: menus[i].is_hidden,
                        is_main_menu: menus[i].is_main_menu,
                    };
                    let subMenuTemp = [];
                    if (menus[i].submenus && menus[i].submenus.length > 0) {
                        const subMenus = menus[i].submenus;
                        for (let s = 0; s < subMenus.length; s++) {
                            subMenuTemp.push({
                                path: subMenus[s].path,
                                identifier: subMenus[s].identifier,
                                name: subMenus[s].name,
                                auth: subMenus[s].auth,
                                is_dropdown: subMenus[s].is_dropdown,
                                is_hidden: subMenus[s].is_hidden,
                                is_main_menu: subMenus[s].is_main_menu,
                            })
                        }
                    }
                    if (subMenuTemp.length > 0) {
                        eachMenu['submenus'] = subMenuTemp
                    } else {
                        eachMenu['submenus'] = []
                    }

                    // Drop down items
                    let dropDownTemp = [];
                    if (menus[i].dropdown_items && menus[i].dropdown_items.length > 0) {
                        const dropDownItems = menus[i].dropdown_items;
                        for (let s = 0; s < subMenus.length; s++) {
                            dropDownTemp.push({
                                path: dropDownItems[s].path,
                                identifier: dropDownItems[s].identifier,
                                name: dropDownItems[s].name,
                                auth: dropDownItems[s].auth,
                                is_dropdown: dropDownItems[s].is_dropdown,
                                is_hidden: dropDownItems[s].is_hidden,
                                is_main_menu: dropDownItems[s].is_main_menu,
                            })
                        }
                    }
                    if (dropDownTemp.length > 0) {
                        eachMenu['dropdown_items'] = dropDownTemp
                    } else {
                        eachMenu['dropdown_items'] = []
                    }
                    // Finally add to menu Group
                    menuGroup.push(eachMenu);
                }
                if (menuGroup.length > 0) {
                    this.$store.commit(mutationTypes.syncMenuItems, menuGroup)
                }
            }
        }
    }
</script>

<style scoped>

</style>