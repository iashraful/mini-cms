<template>
    <div>
        <p class="alert alert-success" v-if="showAlert">{{ alertMgs }}</p>
        <h1>Page List</h1>
        <div class="row">
            <form v-on:submit.prevent="handleSubmit">
                <label>Page Title</label>
                <input v-model="page.name"/>
                <p v-if="errorData.name !== undefined" class="alert-danger">{{errorData.name[0]}}</p>
                <br/>
                <label>Page Path</label>
                <input v-model="page.path"/>
                <p v-if="errorData.path !== undefined" class="alert-danger">{{errorData.path[0]}}</p>
                <br/>
                <button>Add Page</button>
            </form>
        </div>
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
                    name: '', path: ''
                },
                showAlert: false,
                alertMgs: '',
                errorData: {},
            }
        },
        methods: {
            handleSubmit() {
                this.$store.dispatch('addNewPage', this.page).then(() => {
                    this.page = {name: '', path: ''};
                    this.errorData = {};
                    this.$bus.$emit('AddedNewPage', 'New Page Added');
                    this.showAlert = true;
                    this.alertMgs = 'Page created successfully';
                }, (err) => {
                    this.errorData = err;
                })
            },
            convertToSlug(text) {
                return text
                    .toLowerCase()
                    .replace(/[^\w ]+/g, '')
                    .replace(/ +/g, '-');
            }
        },
        watch: {
            ['page.name'](newVal, oldVal) {
                this.page['path'] = this.convertToSlug(newVal);
            }
        },
    }
</script>

<style scoped>

</style>