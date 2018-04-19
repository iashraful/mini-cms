<template>
    <div>
        <div v-if="loading" class="mt-5 text-center" style="font-size: 32px">Loading...</div>
        <div v-if="!loading">
            <div v-if="showAlert" class="alert alert-success text-center">
                {{ alertMgs }}
            </div>
            <h5>Add New Content</h5>
            <hr class="mt-0"/>
            <div class="mt-2 mb-4">
                <form v-on:submit.prevent="onContentSubmit">
                    <label>Title</label>
                    <input type="text" class="form-input" v-model="newContent.title" required/>
                    <label>Description</label>
                    <vue-editor v-model="newContent.body"></vue-editor>
                    <button class="mt-2 pull-right btn btn-outline-success pl-5 pr-5">Save Content</button>
                    <label class="pull-right" style="padding: 16px 21px 0 8px;">Publish</label>
                    <input type="checkbox" class="pull-right" style="margin-top: 21px;" v-model="statusCheckBox"/>
                    <br/>
                </form>
            </div>
            <h5>{{ currentPage.name }} Contents</h5>
            <hr class="mt-0"/>
            <div v-for="(content, index) in currentPage.contents" :key="index" class="mb-4">
                <h6 class="content-title">
                    {{ index + 1 }}. {{ content.title }}
                    <span style="font-size: 12px"
                          :class="{'alert alert-danger p-1': content.status === enums.ContentEnum.DRAFT.value, 'alert alert-info p-1': content.status === enums.ContentEnum.ARCHIVE.value, }">
                        {{ enums.ContentEnum.props[content.status].name }}
                    </span>
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
    import {VueEditor} from 'vue2-editor'
    import * as enums from '@/config/enums'

    export default {
        name: "user-page-details",
        data() {
            return {
                currentPage: this.$store.getters.getCurrentPage,
                newContent: {
                    title: '', body: '', page_slug: this.$route.params.pageSlug, status: enums.ContentEnum.DRAFT.value,
                },
                loading: false,
                enums: enums,
                statusCheckBox: false,
                showAlert: false,
                alertMgs: ''
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
                    this.currentPage.contents.unshift(response);
                    this.newContent = {title: '', body: ''};
                    this.statusCheckBox = false;
                    this.showAlert = true;
                    this.alertMgs = 'Content Saved Successfully';
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
            },
            statusCheckBox(newVal, oldVal) {
                if (newVal === true) {
                    this.newContent.status = enums.ContentEnum.PUBLISH.value
                } else {
                    this.newContent.status = enums.ContentEnum.DRAFT.value
                }
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