<template>
    <div>
        <div v-if="loading" class="mt-5 text-center" style="font-size: 32px">Loading...</div>
        <div v-if="!loading">
            <h5>Add New Content</h5>
            <hr class="mt-0"/>
            <div class="mt-2 mb-4">
                <form v-on:submit.prevent="onContentSubmit">
                    <label>Title</label>
                    <input type="text" class="form-input" v-model="newContent.title" required/>
                    <label>Description</label>
                    <vue-editor v-model="newContent.body"></vue-editor>
                    <button class="mt-2 pull-right btn btn-outline-success pl-5 pr-5">Publish</button>
                    <br/>
                </form>
            </div>
            <h5>{{ currentPage.name }} Contents</h5>
            <hr class="mt-0"/>
            <div>
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
            </div>
        </div>
    </div>
</template>

<script>
    import {VueEditor} from 'vue2-editor'

    export default {
        name: "user-page-details",
        data() {
            return {
                currentPage: this.$store.getters.getCurrentPage,
                newContent: {title: '', body: '', page_slug: this.$route.params.pageSlug},
                loading: false,
            }
        },
        components: {
            VueEditor,
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
            onContentSubmit() {
                this.$store.dispatch('postNewContent', this.newContent).then((response) => {
                    console.log(response)
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
    .form-input {
        width: 100%;
        height: 37px;
    }
    
    .pull-right {
        float: right;
    }
</style>