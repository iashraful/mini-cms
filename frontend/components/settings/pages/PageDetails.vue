<template>
    <div>
        <h1>Page Details</h1>
    </div>
</template>

<script>
    export default {
        name: "page-details",
        watch: {
            '$route'(to, from) {
                let page = this.$store.getters.getPageByPath(to.path);
                if (page === undefined) {
                    this.$router.push('/404')
                }
            }
        }
    }
</script>

<style scoped>

</style>