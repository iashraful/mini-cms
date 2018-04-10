<template>
    <div>
        <p class="alert alert-success" v-if="showAlert">{{ alertMgs }}</p>
        <h1>Page List</h1>
        <div class="row">
            <form v-on:submit.prevent="handleSubmit">
                Page Title: <input v-model="page.name"/>
                Page Path: <input v-model="page.path"/>
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
                alertMgs: ''
            }
        },
        methods: {
            handleSubmit() {
                this.$store.dispatch('addNewPage', this.page).then(() => {
                    this.page = {name: '', path: ''};
                    this.showAlert = true;
                    this.alertMgs = 'Page created successfully';
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
                let slugPath = this.convertToSlug(newVal);
                this.page['path'] = slugPath;
            }
        }
    }
</script>

<style scoped>

</style>