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
    }
</script>

<style scoped>

</style>