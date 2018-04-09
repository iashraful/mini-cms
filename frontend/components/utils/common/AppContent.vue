<template>
    <div v-bind:class="{'app-body': !isAuth, 'app-body-sidebar': isAuth}">
        <slot name="main-content"></slot>
    </div>
</template>

<script>
    export default {
        name: "app-content",
        data() {
            return {
                isAuth: this.$store.state.isAuthenticated
            }
        }
    }
</script>

<style scoped>

</style>