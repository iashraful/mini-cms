<template>
    <div>
        <h2 class="text-center">{{ content.title }}</h2>
        <p v-html="content.body"></p>
        <div>
            <comment-list/>
        </div>
    </div>
</template>

<script>
    import CommentList from "@/components/comments/CommentList";
    export default {
        name: "content-details",
        components: {CommentList},
        data() {
            return {
                content: {}
            }
        },
        methods: {
            getContentDetails() {
                const slug = this.$route.params.contentSlug;
                this.$store.dispatch('getContentDetailsFromApi', slug).then((data) => {
                    this.content = data;
                })
            }
        },
        mounted() {
            this.getContentDetails();
        }
    }
</script>

<style scoped>

</style>