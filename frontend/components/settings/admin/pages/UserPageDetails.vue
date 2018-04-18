<template>
    <div>
        <h5>{{ currentPage.name }} Contents</h5>
        <hr class="mt-0"/>
        <h5>Add New Content</h5>
        <hr class="mt-0"/>
        <div class="mt-2 mb-4">
            <form>
                <label>Title</label>
                <input type="text" class="form-control" v-model="newContent.title"/>
                <label>Description</label>
                <vue-editor v-model="newContent.body"></vue-editor>
            </form>
        </div>
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
</template>

<script>
    import { VueEditor } from 'vue2-editor'

    export default {
        name: "user-page-details",
        data() {
            return {
                currentPage: this.$store.getters.getCurrentPage,
                newContent: {title: '', body: ''}
            }
        },
        components: {
            VueEditor,
        },
        methods: {
            getPageDetails() {
                const path = this.$route.params.pageSlug;
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