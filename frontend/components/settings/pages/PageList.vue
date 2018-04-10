<template>
    <div>
        <h1>Page List</h1>
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
        }
        }
    }
</script>

<style scoped>

</style>