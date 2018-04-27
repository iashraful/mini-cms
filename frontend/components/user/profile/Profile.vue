<template>
    <div class="container">
        <div class="row profile">
            <profile-left-side-view/>
            <profile-content-view/>
        </div>
    </div>
</template>

<script>
    import ProfileLeftSideView from "@/components/user/profile/ProfileLeftSideView";
    import ProfileContentView from "@/components/user/profile/ProfileContentView";

    export default {
        name: "Profile",
        components: {ProfileContentView, ProfileLeftSideView}
    }
</script>

<style scoped>
    body {
        background: #f7f7f7 !important;
    }

    /* Profile container */
    .profile {
        margin: 20px 0;
    }
</style>