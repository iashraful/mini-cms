<template>
    <div class="row">
        <div class="col-12">
            <div class="card">
                <div class="card-header">
                    <h4>Comment Area</h4>
                </div>
                <div class="card-body">
                    <form v-on:submit.prevent="handleCommentSubmit">
                        <div class="form-group">
                            <label>Email</label>
                            <small class="d-block text-muted">Your email will keep private forever</small>
                            <input type="email" class="form-control" v-model="newComment.email" required/>
                        </div>
                        <div class="form-group">
                            <label>Full Name</label>
                            <input type="text" class="form-control" v-model="newComment.name"/>
                        </div>
                        <div class="form-group">
                            <label>Comment</label>
                            <textarea rows="3" class="form-control"
                                      placeholder="write you comment here..."
                                      v-model="newComment.comment">
                            </textarea>
                        </div>
                        <button type="submit" class="float-right btn btn-success big-button">Comment</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "CommentList",
        data() {
            return {
                newComment: {
                    comment: '', name: '', email: ''
                }
            }
        },
        methods: {
            handleCommentSubmit() {
                console.log(this.newComment)
            }
        }
    }
</script>

<style scoped>
    .card-header {
        padding: 5px 6px 0 5px !important;
    }

    .card-body {
        padding: .75rem !important;
    }

    .big-button {
        padding: .5rem 5rem;
    }
</style>