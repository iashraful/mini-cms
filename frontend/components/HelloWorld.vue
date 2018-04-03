<template>
    <div>
        <h1 class="c-red">{{ msg }}</h1>
        <h2>CLick Count: {{ count }}</h2>
        <button class="btn btn-outline-danger" v-on:click="tryIncrement">Increment</button>
    </div>
</template>

<script>
    import AppContent from "@/components/utils/common/AppContent"
    import store from '@/store/index'
    import * as mutationTypes from '@/store/mutations-types'

    export default {
        components: {
            AppContent
        },
        name: 'HelloWorld',
        data() {
            return {
                msg: 'Hello, World!',
                count: 0
            }
        },
        methods: {
            tryIncrement() {
                store.commit(mutationTypes.increment);
                this.count = store.state.count;
            }
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    h1, h2 {
        font-weight: normal;
    }

    ul {
        list-style-type: none;
        padding: 0;
    }

    li {
        display: inline-block;
        margin: 0 10px;
    }

    a {
        color: #42b983;
    }
</style>
