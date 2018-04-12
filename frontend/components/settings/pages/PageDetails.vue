<template>
    <div>
        <h2>Welcome {{ currentPage.name }}</h2>
        <!--<p v-if="currentPage.contents.length < 1">No Content found</p>-->
    </div>
</template>

<script>
    export default {
        name: "page-details",
        data() {
            return {
                currentPage: this.$store.getters.getCurrentPage
            }
        },
        methods: {
            getPageDetails() {
                const path = this.$router.history.current.path.substring(3);
                this.$store.dispatch('getPageDetailsApiCall', path).then((response) => {
                    if (response.path !== path) {
                        this.$router.push('/404')
                    }
                    this.currentPage = response;
                })
            }
        },
        mounted() {
            const path = this.$router.history.current.path;
            // get current page from api
            this.getPageDetails();
        },
        watch: {
            '$route'(to, from) {
                // get current page from api
                this.getPageDetails();
            }
        }
    }
</script>

<style scoped>

</style>