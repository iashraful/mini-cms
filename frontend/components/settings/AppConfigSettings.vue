<template src="../../templates/settings/app-config-settings.html"></template>

<script>
    import axios from 'axios'
    import store from '@/store/index'
    import * as mutationTypes from '@/store/mutations-types'
    import AppAlert from "@/components/utils/ui/AppAlert";
    import SyncMenu from "@/components/utils/SyncMenu";

    export default {
        components: {AppAlert, SyncMenu},
        name: 'app-config-settings',
        data() {
            return {
                logoFile: store.state.appLogo,
                logo: '',
                logoResponse: {
                    'alert': false,
                    'status': '',
                    'message': ''
                }
            }
        },
        methods: {
            previewImage(input) {
                this.logo = input;
                // Reference to the DOM input element
                // Ensure that you have a file before attempting to read it
                if (input) {
                    // create a new FileReader to read this image and convert to base64 format
                    let reader = new FileReader();
                    // Define a callback function to run, when FileReader finishes its job
                    reader.onload = (e) => {
                        this.logoFile = e.target.result;
                    };
                    // Start the reader job - read file as a data url (base64 format)
                    reader.readAsDataURL(input);
                }
            },
            uploadLogo() {
                if (this.logo === '' || this.logo === undefined || this.logo === null) {
                    this.logoResponse = {
                        'alert': true,
                        'status': 'error',
                        'message': 'You must select your company logo.'
                    };
                    return
                }
                // Here will be save API call
                const url = 'api/app-logo/';
                let formData = new FormData();
                formData.append('logo', this.logo);
                const payload = {
                    headers: {
                        'Content-Type': 'multipart/form-data',
                        // Still I am catching the token on fly from local storage
                        'Authorization': 'Token ' + store.state.token
                    }
                };
                axios.put(url, formData, payload).then((response) => {
                    if (response.data.logo) {
                        this.logoResponse = {
                            'alert': true,
                            'message': 'Logo updated successfully.',
                            'status': 'success'
                        };
                        store.commit(mutationTypes.updateLogo, response.data);
                    }

                }).catch((err) => {
                    this.logoResponse = {
                        'alert': true,
                        'message': err.message,
                        'status': 'error'
                    };
                    console.log(err);
                });
            },
        },
    }
</script>

<style scoped>

</style>
