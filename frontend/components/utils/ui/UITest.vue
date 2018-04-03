<template>
    <div>
        <ui-table
                :uiTableProps="uiTableProps"
                @onPageChange="updatePageNumber"
                @actionButtonTrigger="handleActionTrigger"
                actionColName="Actions"
                identifierName="id"
        >
        </ui-table>

    </div>
</template>

<script>
    import UiTable from "@/components/utils/ui/UiTable";

    export default {
        components: {UiTable},
        name: 'ui-test',
        data() {
            return {
                pageNo: 0,
                uiTableProps: {
                    title: "UI Table",
                    lineNumbers: "true",
                    defaultSortBy: "{field: 'age', type: 'asc'}",
                    globalSearch: "true",
                    paginate: "true",
                    columns: [
                        {
                            label: 'Name',
                            field: 'name',
                        },
                        {
                            label: 'Age',
                            field: 'age',
                            type: 'number',
                            html: false,
                        },
                        {
                            label: 'Created On',
                            field: 'createdAt',
                            type: 'date',
                            inputFormat: 'YYYY-MM-DD',
                            outputFormat: 'MMM Do YY',
                        },
                        {
                            label: 'Percent',
                            field: 'score',
                            type: 'percentage',
                            html: false,
                        },
                        {
                            label: 'Actions',
                            field: 'actions',
                            html: true,
                            sortable: false,
                            thClass: 'wd-200px'
                        },
                    ],
                    rows: [
                        {id: 1, name: "John", age: 20, createdAt: '201-10-31:9:35 am', score: 0.03343, actions:  ['VIEW', 'EDIT', 'DEL']},
                        {id: 2, name: "Jane", age: 24, createdAt: '2011-10-31', score: 0.03343, actions: ['VIEW', 'EDIT', 'DEL']},
                        {id: 3, name: "Susan", age: 16, createdAt: '2011-10-30', score: 0.03343, actions:  ['VIEW', 'EDIT', 'DEL']},
                        {id: 4, name: "Chris", age: 55, createdAt: '2011-10-11', score: 0.03343, actions:  ['VIEW', ]},
                        {id: 5, name: "Dan", age: 40, createdAt: '2011-10-21', score: 0.03343, actions:  ['VIEW', 'EDIT', 'DEL']},
                        {id: 6, name: "John", age: 20, createdAt: '2011-10-31', score: 0.03343, actions:  ['VIEW', ]},
                        {id: 7, name: "Jane", age: 24, createdAt: '20111031', actions:  ['VIEW', 'Edit', 'DEL']},
                        {id: 8, name: "Susan", age: 16, createdAt: '2013-10-31', score: 0.03343, actions:  ['VIEW', 'EDIT',]},
                        {id: 9, name: "Chris", age: 55, createdAt: '2012-10-31', score: 0.03343, actions:  ['VIEW', 'EDIT', 'DEL']},
                        {id: 10, name: "Dan", age: 40, createdAt: '2011-10-31', score: 0.03343, actions:  ['Edit', 'DEL']},
                        {id: 11, name: "John", age: 20, createdAt: '2011-10-31', score: 0.03343, actions:  ['VIEW', 'EDIT', 'DEL']},
                        {id: 12, name: "Jane", age: 24, createdAt: '2011-07-31', score: 0.03343, actions:  ['VIEW', 'EDIT', 'DEL']},
                        {id: 13, name: "Susan", age: 16, createdAt: '2017-02-28', score: 0.03343, actions:  ['VIEW', 'EDIT', 'DEL']},
                        {id: 14, name: "Chris", age: 55, createdAt: '', score: 0.03343, actions:  ['VIEW', 'Edit', 'DEL']},
                        {id: 15, name: "Dan", age: 40, createdAt: '2011-10-31', score: 0.03343, actions:  ['VIEW', 'EDIT', 'DEL']},
                        {id: 19, name: "Chris", age: 55, createdAt: '2011-10-31', score: 0.03343, actions:  ['VIEW', 'EDIT', 'DEL']},
                        {id: 20, name: "Dan", age: 40, createdAt: '2011-10-31', score: 0.03343, actions:  ['VIEW', 'EDIT', 'DEL']},
                    ],
                },
            }
        },
        methods: {
            updatePageNumber(val) {
                this.pageNo = val;
            },
            handleActionTrigger(actionType, id) {
                console.log(actionType, id);
            }
        }
    }
</script>

<style scoped>

</style>