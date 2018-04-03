<template>
    <div>
        <h2 class="text-center">Successfully logged out.</h2>
    </div>
</template>

<script>
    export default {
        name: "logout",
        mounted() {
            // Illusion of logout feature
            localStorage.setItem('user_role', "");
            localStorage.setItem('token', "");
            localStorage.setItem('auth', "false");
            // this.$router.push('/');
            window.location.href = '/';
        }
    }
</script>

<style scoped>

</style>