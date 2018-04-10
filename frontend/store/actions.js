import * as mutationTypes from './mutations-types'
import pagesApi from '@/services/api-helper/pages'

export default {
    addNewPage(context, page) {
        return new Promise((success, fail) => {
            context.commit(mutationTypes.addPage, page);
            // Then,
            success();
        })
    },

    getPagesApiCall(context) {
        return new Promise((success, fail) => {
            pagesApi.getPages().then((pages) => {
                context.commit(mutationTypes.getPages, pages);
            });
            success();
        })
    }
}