import * as mutationTypes from './mutations-types'
import pagesApi from '@/services/api-helper/pages'

export default {
    addNewPage(context, page) {
        return new Promise((success, fail) => {
            pagesApi.postPage(page).then((response) => {
                console.log(response);
                context.commit(mutationTypes.addPage, response);
                success();
            });
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