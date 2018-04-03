<template>
    <div :class="alertClass" role="alert">
        <div class="text-center">{{ message }}</div>
        <button type="button" class="close" data-dismiss="alert" aria-label="Close">
            <span aria-hidden="true">&times;</span>
        </button>
    </div>
</template>

<script>
    export default {
        props: ['status', 'message'],
        name: 'app-alert',
        data () {
            return {
                alertClass: 'alert alert-dismissible fade show '
            }
        },
        mounted () {
            // Here status will received and generate css Class
            if (this.status === 'success') {
                this.alertClass += 'alert-success'
            }
            else if (this.status === 'warning') {
                this.alertClass += 'alert-warning'
            }
            else if (this.status === 'error') {
                this.alertClass += 'alert-danger'
            }
            else {
                this.alertClass += 'alert-primary'
            }
        }
    }
</script>

<style scoped>

</style>