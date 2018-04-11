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
            handler404(path) {
                let page = this.$store.getters.getPageByPath(path);
                if (page === undefined) {
                    this.$router.push('/404')
                }
            },
            getPageDetails() {
                const path = this.$router.history.current.path.substring(1);
                this.$store.dispatch('getPageDetailsApiCall', path).then((response) => {
                    this.currentPage = this.$store.state.currentPage;
                })
            }
        },
        mounted() {
            const path = this.$router.history.current.path;
            this.handler404(path.substring(1));
            // get current page from api
            this.getPageDetails();
        },
        watch: {
            '$route'(to, from) {
                this.handler404(to.path.substring(1));
                // get current page from api
                this.getPageDetails();
            }
        }
    }
</script>

<style scoped>

</style>