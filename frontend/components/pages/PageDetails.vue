<template>
    <div>
        <div v-if="loading" class="mt-5 text-center" style="font-size: 32px">Loading...</div>
        <div v-if="!loading">
            <h5>{{ currentPage.name }}</h5>
            <hr class="mt-0"/>
            <div v-if="currentPage.contents.length <= 0" class="text-center">
                No content Found.
            </div>
            <div v-for="(content, index) in currentPage.contents" :key="index" class="mb-4">
                <h6 class="content-title">
                    <span v-if="currentPage.contents.length > 1">{{ index + 1 }}.</span> {{ content.title }}
                </h6>
                <p v-if="content.body.length > 500" class="text-muted mb-0 ml-4"
                   v-html="content.body.slice(0, 500) + '...'"></p>
                <p v-if="content.body.length <= 500" class="text-muted mb-0 ml-4"
                   v-html="content.body.slice(0, 500)"></p>
                <button v-if="content.body.length > 500"
                        v-on:click="handleReadMore(content.identifier)"
                        class="ml-4 btn btn-outline-primary pt-0 pb-0 pl-5 pr-5">
                    Read More
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
            },
            handleReadMore(slug) {
                this.$router.push('/c/' + slug)
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