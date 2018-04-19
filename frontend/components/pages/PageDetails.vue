<template>
    <div>
        <div v-if="loading" class="mt-5 text-center" style="font-size: 32px">Loading...</div>
        <div v-if="!loading">
            <h5>{{ currentPage.name }}</h5>
            <hr class="mt-0"/>
            <div v-for="(content, index) in currentPage.contents" :key="index">
                <h6 class="content-title">{{ index + 1 }}. {{ content.title }}</h6>
                <p v-if="content.body.length > 500" class="text-muted mb-0 ml-4"
                   v-html="content.body.slice(0, 500) + '...'"></p>
                <p v-if="content.body.length <= 500" class="text-muted mb-0 ml-4"
                   v-html="content.body.slice(0, 500)"></p>
                <button v-if="content.body.length > 500"
                        class="ml-4 btn btn-outline-primary pt-0 pb-0 pl-5 pr-5">
                    View Details
                </button>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "page-details",
        data() {
            return {
                currentPage: this.$store.getters.getCurrentPage,
                loading: false,
            }
        },
        methods: {
            getPageDetails() {
                this.loading = true;
                const path = this.$route.params.pageSlug;
                this.$store.dispatch('getPageDetailsApiCall', path).then((response) => {
                    if (response.path !== path) {
                        this.$router.push('/404')
                    }
                    this.loading = false;
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