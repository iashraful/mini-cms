<template src="@/templates/settings/app-config-settings.html"></template>

<script>
    import AppAlert from "@/components/utils/ui/AppAlert";

    export default {
        components: {AppAlert},
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
