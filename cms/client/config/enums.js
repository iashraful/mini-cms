export const ContentEnum = {
    DRAFT: {value: 0, name: 'Draft', code: 'DFT'},
    PUBLISH: {value: 1, name: 'Published', code: 'PSH'},
    ARCHIVE: {value: 2, name: 'Archived', code: 'AVE'},
    props: {
        0: {name: 'Draft', value: 0, code: 'DFT'},
        1: {name: 'Published', value: 1, code: 'PSH'},
        2: {name: 'Archived', value: 2, code: 'AVE'}
    }
};

export const ActionTypeEnum = {
    CREATE: {value: 0, name: 'Create', code: 'CRT'},
    EDIT: {value: 1, name: 'Edit', code: 'EDT'},
    DELETE: {value: 2, name: 'Delete', code: 'DLT'},
    props: {
        0: {value: 0, name: 'Create', code: 'CRT'},
        1: {value: 1, name: 'Edit', code: 'EDT'},
        2: {value: 2, name: 'Delete', code: 'DLT'}
    }
};
