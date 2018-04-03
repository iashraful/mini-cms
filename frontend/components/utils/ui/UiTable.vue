<template>
    <div>
        <vue-good-table
                v-bind="uiTableProps"
                @pageChanged="onPageChange">
            <!-- ROW Template -->
            <template slot="table-row" slot-scope="props">
                <td v-for="col in uiTableProps.columns">
                     <span v-if="col.label === actionColName">
                         <span v-for="btn in props.row[col.field]">
                             <button v-if="btn === 'VIEW'"
                                     v-on:click="actionButtonTrigger(btn, props.row[identifierName])"
                                     class="btn btn-xs btn-default action-table-btn-sz">View</button>
                             <button v-if="btn === 'EDIT'"
                                     v-on:click="actionButtonTrigger(btn, props.row[identifierName])"
                                     class="btn btn-xs btn-outline-primary action-table-btn-sz">Edit</button>
                             <button v-if="btn === 'DEL'"
                                     v-on:click="actionButtonTrigger(btn, props.row[identifierName])"
                                     class="btn btn-xs btn-outline-danger action-table-btn-sz">Del</button>
                         </span>
                     </span>
                    <span v-else>{{ props.row[col.field] }}</span>
                </td>
            </template>
        </vue-good-table>
    </div>
</template>

<script>
    /**
     * https://github.com/xaksis/vue-good-table
     * All the props will work as same as documentation. But you have to send props like
     <ui-table uiTableProps="YourProps"/>. That's it. You are hero now. It will work fine. :)
     */
    import Vue from 'vue';
    import VueGoodTable from 'vue-good-table';

    Vue.use(VueGoodTable);
    export default {
        name: "ui-table",
        props: ['uiTableProps', 'pageChanged', 'actionColName', 'identifierName'],
        data() {
            return {};
        },
        methods: {
            onPageChange: function (evt) {
                // { currentPage: 1, currentPerPage: 10, total: 5 }
                this.$emit('onPageChange', evt.currentPage)
            },
            actionButtonTrigger(actionType, id) {
                // actionType can be EDIT, VIEW, DEL etc...
                this.$emit('actionButtonTrigger', actionType, id)
            }
        }
    }
</script>

<style scoped>

</style>