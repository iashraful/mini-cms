<template>
    <div class="app-footer">
        <p>
            <span>Developed by, <strong>Ashraful Islam</strong></span>
            <span> | </span>
            <span>
                <a href="https://iashraful.me" target="_blank">Portfolio</a> |
                <a href="https://github.com/iamashraful" target="_blank">Github</a> |
                <a href="mailto:ashrafulrobin3@gmail.com">Email me</a>
            </span>
        </p>
    </div>
</template>

<script>
    export default {
        name: "app-footer"
    }
</script>

<style scoped>
    .app-footer {
        position: relative;
        padding-top: 1rem;
        bottom: 0;
        width: 100%;
    }
    .app-footer p {
        float: right;
    }
</style>