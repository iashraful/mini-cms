<template src="@/templates/settings/app-config-settings.html"></template>

<script>
    import AppAlert from "cms/frontend/components/utils/ui/AppAlert";
    import {VueEditor} from 'vue2-editor';

    export default {
        components: {AppAlert, VueEditor},
        name: 'app-config-settings',
        data() {
            return {
                appConfig: this.$store.state.appConfig,
                showAlert: false,
                alertMgs: '',
            }
        },
        methods: {
            getAppConfigs() {

            },

            handleAppConfigSubmit() {
                this.$store.dispatch('updateAppConfigPostApi', this.appConfig).then((data) => {
                    this.$bus.$emit('EB_ConfigUpdated', 'App Config Updated');
                    this.showAlert = true;
                    this.alertMgs = 'Updated successfully';
                })
            }
        },
    }
</script>

<style scoped>

</style>
