import * as mutationTypes from './mutations-types'

export default {
    addNewPage(context, page) {
        return new Promise((success, reject) => {
            context.commit(mutationTypes.addPage, page);
            // Then,
            success();
        })
    }
}