<template>
    <div>
        <div v-if="loading" class="mt-5 text-center" style="font-size: 32px">Loading...</div>
        <div v-if="!loading">
            <h5>{{ currentPage.name }}</h5>
            <hr class="mt-0"/>
            <h6>1. Post Title</h6>
            <p class="text-muted mb-0">
                Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the
                industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and
                scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into
                electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of
                Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like
                Aldus PageMaker including versions of Lorem Ipsum.
            </p>
            <button class="btn btn-outline-primary pt-1 pb-1 pl-5 pr-5">View Details</button>
            <h6 class="mt-3">2. Post Title 2</h6>
            <p class="text-muted mb-0">
                Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the
                industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and
                scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into
                electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of
                Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like
                Aldus PageMaker including versions of Lorem Ipsum.
            </p>
            <button class="btn btn-outline-primary pt-1 pb-1 pl-5 pr-5">View Details</button>
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