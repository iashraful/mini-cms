<template>
    <div>
        <form class="form-signin" v-on:submit.prevent="loginFormSubmit" v-show="!isAuth">
            <h2 class="form-signin-heading">Please sign in</h2>
            <label class="sr-only">Username</label>
            <input type="text" class="form-control" v-model="username"
                   placeholder="Username..." required autofocus>
            <label class="sr-only">Password</label>
            <input type="password" class="form-control" v-model="password"
                   placeholder="Password..." required>
            <p v-show="!success" class="alert alert-danger">{{ errorData.message }}</p>
            <button class="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>
        </form>
    </div>
</template>

<script>
    import store from 'cms/frontend/store'
    import * as mutationTypes from 'cms/frontend/store/mutations-types'

    export default {
        name: "login",
        data() {
            return {
                "username": "",
                "password": "",
                errorData: "",
                success: true,
                isAuth: store.state.isAuthenticated
            }
        },
        methods: {
            setToLocalStorage(data) {
                let now = new Date();
                let nowTimestamp = now.getTime();
                const oneDayInterval = 24 * 60 * 60 * 1000;
                const after24Hour = nowTimestamp + oneDayInterval;
                localStorage.setItem('user_role', String(data.user_role));
                localStorage.setItem('token', String(data.token));
                localStorage.setItem('auth', "true");
                localStorage.setItem('loginTime', String(after24Hour));
                // save to store
                store.commit(mutationTypes.login, data);
            },
            loginFormSubmit() {
                const loginUrl = '/api/login/';
                const payload = {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({
                        username: this.username,
                        password: this.password
                    })
                };
                fetch(loginUrl, payload).then((response) => {
                    return response.json();
                }).then((data) => {
                    if (data.token) {
                        this.setToLocalStorage(data);
                        window.location.href = '/';
                    }
                    else {
                        this.errorData = data;
                        this.success = false;
                    }
                })
            }
        },
        created() {
            // Token expired logic
            let now = new Date();
            let nowTimestamp = now.getTime();
            const oneDayInterval = 24 * 60 * 60 * 1000;
            let lastLogin = parseInt(localStorage.getItem('loginTime'));
            if ((nowTimestamp - oneDayInterval) > lastLogin) {
                localStorage.clear();
                window.location.href = '/'
            }
        },
        mounted() {
            // if (this.isAuth) {
            //     this.$router.push('/')
            // }
        }
    }
</script>

<style scoped>
    body {
        padding-top: 40px;
        padding-bottom: 40px;
        background-color: #eee;
    }

    .form-signin {
        max-width: 330px;
        padding: 15px;
        margin: 0 auto;
    }

    .form-signin .form-signin-heading,
    .form-signin .checkbox {
        margin-bottom: 10px;
    }

    .form-signin .checkbox {
        font-weight: normal;
    }

    .form-signin .form-control {
        position: relative;
        height: auto;
        -webkit-box-sizing: border-box;
        box-sizing: border-box;
        padding: 10px;
        font-size: 16px;
    }

    .form-signin .form-control:focus {
        z-index: 2;
    }

    .form-signin input[type="email"] {
        margin-bottom: -1px;
        border-bottom-right-radius: 0;
        border-bottom-left-radius: 0;
    }

    .form-signin input[type="password"] {
        margin-bottom: 10px;
        border-top-left-radius: 0;
        border-top-right-radius: 0;
    }
</style>