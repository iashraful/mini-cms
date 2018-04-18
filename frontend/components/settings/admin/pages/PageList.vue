<template>
    <div>
        <p class="alert alert-success text-center" v-if="showAlert">{{ alertMgs }}</p>
        <h5>Add new page</h5>
        <hr class="mt-0"/>
        <div class="">
            <form v-on:submit.prevent="handleSubmit">
                <label>Title</label>
                <input class="form-input" v-model="page.name"/>
                <p v-if="errorData.name !== undefined" class="alert-danger">{{errorData.name[0]}}</p>
                <button class="btn btn-primary btn-sm">Add Page</button>
            </form>
        </div>
        <h5 class="mt-2">Page List</h5>
        <hr class="mt-0"/>
        <ul>
            <li v-for="page in pages">
                <router-link :to="currentPath + '/' + page.path">{{page.name}}</router-link>
            </li>
        </ul>
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
                    this.$bus.$emit('addedNewPage_EB', 'New Page Added');
                    this.showAlert = true;
                    this.alertMgs = 'Page created successfully';
                }, (err) => {
                    this.errorData = err;
                })
            }
        },
        created() {
            this.$bus.$on('renderedPages', () => {
                this.pages = this.$store.state.pages;
            })
        }
    }
</script>

<style scoped>
    .form-input {
        padding: .175rem .55rem;;
        font-size: 1rem;
        line-height: 1.5;
        color: #495057;
        background-color: #fff;
        background-clip: padding-box;
        border: 1px solid #ced4da;
        border-radius: .25rem;
        transition: border-color .15s ease-in-out, box-shadow .15s ease-in-out;
    }
</style>