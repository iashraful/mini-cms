<template>
    <div>
        <p class="alert alert-success text-center" v-if="showAlert">{{ alertMgs }}</p>
        <h5>Add new page</h5>
        <hr class="mt-0"/>
        <div class="">
            <form v-on:submit.prevent="handleSubmit">
                <div class="form-group">
                    <label>Title</label>
                    <input class="form-input" v-model="page.name"/>
                    <p v-if="errorData.name !== undefined" class="alert-danger">{{errorData.name[0]}}</p>
                </div>
                <button class="btn btn-primary btn-sm">Add Page</button>
            </form>
        </div>
        <div class="row">
            <div class="col-md-12">
                <div class="row">
                    <div class="col-sm-6">
                        <h5 class="mt-2">Page List</h5>
                        <hr class="mt-0"/>
                    </div>
                    <div class="col-sm-6" v-if="editablePageSlug !== null">
                        <h5 class="mt-2">Update Page</h5>
                        <hr class="mt-0"/>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-6 col-sm-6 col-xs-12">
                        <table class="table">
                            <thead class="thead-dark">
                            <tr>
                                <th scope="col">Order</th>
                                <th scope="col">Title</th>
                                <th scope="col">Actions</th>
                            </tr>
                            </thead>
                            <tbody>
                            <tr v-for="page in pages">
                                <th scope="row">{{ page.order }}</th>
                                <td>{{ page.name }}</td>
                                <td style="width: 180px !important;">
                                    <router-link :to="currentPath + '/' + page.path" class="btn btn-info btn-xs">
                                        View
                                    </router-link>
                                    <button v-on:click="editInlinePage(page.path)"
                                            class="btn btn-warning  btn-xs">
                                        Edit
                                    </button>
                                    <button v-on:click="onPageDelete(page.path)"
                                            class="btn btn-danger  btn-xs">
                                        Del
                                    </button>
                                </td>
                            </tr>
                            </tbody>
                        </table>
                    </div>
                    <!-- Update Part -->
                    <div class="col-md-6 col-sm-6 col-xs-12" v-if="editablePageSlug !== null">
                        <form v-on:submit.prevent="submitUpdatePage">
                            <div class="form-group">
                                <label>Page Title</label>
                                <input type="text" class="form-control" v-model="pageUpdateFormData.name"/>
                            </div>
                            <button type="submit" class="btn btn-sm btn-outline-dark">Update</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "page-list",
        data() {
            return {
                pages: this.$store.state.pages,
                currentPath: this.$router.history.current.path,
                page: {
                    name: '',
                },
                editablePageSlug: null,
                pageUpdateFormData: {
                    name: '',
                },
                showAlert: false,
                alertMgs: '',
                errorData: {},
            }
        },
        methods: {
            handleSubmit() {
                this.$store.dispatch('addNewPage', this.page).then(() => {
                    this.page = {name: ''};
                    this.errorData = {};
                    this.$bus.$emit('EB_PageChanged', 'New Page Added');
                    this.showAlert = true;
                    this.alertMgs = 'Page created successfully';
                }, (err) => {
                    this.errorData = err;
                })
            },
            editInlinePage(pageSlug) {
                this.editablePageSlug = pageSlug;
                this.pageUpdateFormData = this.$store.getters.getPageByPath(pageSlug);
            },
            onPageDelete(pageSlug) {
                swal({
                    title: "Are you sure?",
                    text: "Once deleted, you will not be able to recover it's contents.",
                    icon: "warning",
                    buttons: true,
                    dangerMode: true,
                }).then((willDelete) => {
                    if (willDelete) {
                        this.$store.dispatch('deletePage', pageSlug).then(() => {
                            this.$bus.$emit('EB_PageChanged', 'Page Deleted');
                            swal("Content has deleted successfully.", {
                                icon: "success",
                            });
                        });
                    } else {
                        swal("Thanks God! You changed mind to delete this.");
                    }
                });
            },
            submitUpdatePage() {
                const payload = {
                    pageSlug: this.editablePageSlug,
                    page: this.pageUpdateFormData
                };
                this.$store.dispatch('updatePage', payload).then((data) => {
                    this.showAlert = true;
                    this.alertMgs = 'Page Updated Successfully.';
                    this.editablePageSlug = null;
                    this.$bus.$emit('EB_PageChanged', 'Page Updated');
                });
            }
        },
        created() {
            this.$bus.$on('EB_RenderedPages', () => {
                this.pages = this.$store.state.pages;
            })
        }
    }
</script>

<style scoped>
    .form-input {
        display: block;
        width: 50%;
        padding: .375rem .75rem;
        font-size: 1rem;
        line-height: 1.5;
        color: #495057;
        background-color: #fff;
        background-clip: padding-box;
        border: 1px solid #ced4da;
        border-radius: .25rem;
        transition: border-color .15s ease-in-out, box-shadow .15s ease-in-out;
    }

    .row {
        margin-left: -15px !important;
        margin-right: -15px !important;
    }
</style>