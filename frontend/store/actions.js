import * as mutationTypes from './mutations-types'
import pagesApi from '@/services/api-helper/pages'

export default {
    addNewPage(context, page) {
        return new Promise((success, fail) => {
            pagesApi.postPage(page).then((response) => {
                if (response.id) {
                    context.commit(mutationTypes.addPage, response);
                    success();
                }
            }, (error) => {
                fail(error)
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
    },

    getPageDetailsApiCall(context, path) {
        return new Promise((success, fail) => {
            pagesApi.getPageDetails(path).then((page) => {
                context.commit(mutationTypes.getPageDetails, page);
            });
            success();
        })
    }
}