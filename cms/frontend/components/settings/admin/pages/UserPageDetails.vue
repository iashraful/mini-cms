<template>
    <div class="row">
        <div v-if="loading" class="mt-5 text-center" style="font-size: 32px">Loading...</div>
        <div v-if="!loading" class="col-md-8 col-sm-12">
            <div v-if="showAlert" class="alert alert-success text-center">
                {{ alertMgs }}
            </div>
            <h5>{{ contentFormTitle }}</h5>
            <hr class="mt-0"/>
            <div class="mt-2 mb-4">
                <form v-on:submit.prevent="onContentSubmit(actionType)">
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
        </div>
        <div class="col-md-4 col-sm-12">
            <h5>{{ currentPage.name }} Contents</h5>
            <hr class="mt-0"/>
            <div class="text-center" v-if="currentPage.contents.length <= 0">
                No contents found.
            </div>
            <div v-for="(content, index) in currentPage.contents" :key="index" class="mb-4">
                <h6 class="content-title">
                    <span v-if="currentPage.contents.length > 1">{{ index + 1 }}.</span> {{ content.title }}
                    <span style="font-size: 12px"
                          :class="{'alert alert-danger p-1': content.status === enums.ContentEnum.DRAFT.value, 'alert alert-info p-1': content.status === enums.ContentEnum.ARCHIVE.value, }">
                        {{ enums.ContentEnum.props[content.status].name }}
                    </span>
                </h6>
                <p v-if="content.body.length > 100" class="text-muted mb-0 ml-4"
                   v-html="content.body.slice(0, 100) + '...'"></p>
                <p v-if="content.body.length <= 100" class="text-muted mb-0 ml-4"
                   v-html="content.body.slice(0, 100)"></p>
                <button v-on:click="handleEdit(content.identifier)"
                        class="ml-4 btn btn-outline-primary pt-0 pb-0 pl-5 pr-5">
                    Edit
                </button>
                <button v-on:click="handleDelete(content.identifier)"
                        class="ml-4 btn btn-outline-danger pt-0 pb-0 pl-5 pr-5">
                    Delete
                </button>
            </div>
        </div>
    </div>
</template>

<script>
    import {VueEditor} from 'vue2-editor'
    import * as enums from 'cms/frontend/config/enums'
    import swal from 'sweetalert';

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
                alertMgs: '',
                actionType: enums.ActionTypeEnum.CREATE.value,
                contentFormTitle: 'Add New Content',
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
            onContentSubmit(actionType) {
                if (actionType === enums.ActionTypeEnum.CREATE.value) {
                    this.$store.dispatch('postNewContent', this.newContent).then((response) => {
                        this.currentPage.contents.unshift(response);
                        this.newContent = {title: '', body: ''};
                        this.statusCheckBox = false;
                        this.showAlert = true;
                        this.alertMgs = 'Content Saved Successfully';
                    })
                }
                if (actionType === enums.ActionTypeEnum.EDIT.value) {
                    const payload = {
                        data: this.newContent, slug: this.newContent.identifier
                    };
                    this.$store.dispatch('putPageContent', payload).then((response) => {
                        const contentIndex = this.currentPage.contents.findIndex(c => c.identifier === response.identifier);
                        this.currentPage.contents[contentIndex] = response;
                        this.newContent = {title: '', body: ''};
                        this.statusCheckBox = false;
                        this.showAlert = true;
                        this.alertMgs = 'Content Updated Successfully';
                    })
                }
            },
            handleEdit(identifier) {
                this.actionType = enums.ActionTypeEnum.EDIT.value;
                this.contentFormTitle = 'Update Content';
                const content = this.$store.getters.getContentByIdentifier(identifier);
                this.newContent = content;
                this.newContent['page_slug'] = this.currentPage.path;
                this.statusCheckBox = content.status;
            },
            handleDelete(identifier) {
                swal({
                    title: "Are you sure?",
                    text: "Once deleted, you will not be able to recover this content.",
                    icon: "warning",
                    buttons: true,
                    dangerMode: true,
                }).then((willDelete) => {
                    if (willDelete) {
                        this.$store.dispatch('deletePageContent', identifier).then((response) => {
                            const contentIndex = this.currentPage.contents.findIndex(c => c.identifier === identifier);
                            this.currentPage.contents.splice(contentIndex, 1);
                            swal("Content has deleted successfully.", {
                                icon: "success",
                            });
                        });
                    } else {
                        swal("Thanks God! You changed mind to delete this.");
                    }
                });
            }
        },
        mounted() {
            // get current page from api
            this.getPageDetails();
        },
        watch: {
            '$route'(to, from) {
                // get current page from api
                this.getPageDetails();
            },
            statusCheckBox(newVal, oldVal) {
                if (newVal) {
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