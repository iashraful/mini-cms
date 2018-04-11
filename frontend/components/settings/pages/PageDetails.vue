<template>
    <div>
        <h1>Page Details</h1>
    </div>
</template>

<script>
    export default {
        name: "page-details",
        methods: {
            handler404(path) {
                let page = this.$store.getters.getPageByPath(path);
                if (page === undefined) {
                    this.$router.push('/404')
                }
            }
        },
        created() {
            const path = this.$router.history.current.path;
            this.handler404(path);
        },
        watch: {
            '$route'(to, from) {
                this.handler404(to.path)
            }
        }
    }
</script>

<style scoped>

</style>