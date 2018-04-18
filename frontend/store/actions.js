import * as mutationTypes from './mutations-types'
import pagesApi from '@/services/api-helper/pages'
import contentApi from '@/services/api-helper/contents'

export default {
    addNewPage(context, page) {
        return new Promise((success, fail) => {
            pagesApi.postPage(page).then((response) => {
                if (response.path) {
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
                success(pages);
            });

        })
    },

    getPageDetailsApiCall(context, path) {
        return new Promise((success, fail) => {
            pagesApi.getPageDetails(path).then((page) => {
                context.commit(mutationTypes.getPageDetails, page);
                success(page);
            }).then((err) => {
                fail(err)
            });
        })
    },

    postNewContent(context, data) {
        return new Promise((success, fail) => {
            contentApi.postContent(data).then((content) => {
                context.commit(mutationTypes.saveContent, content);
                success(content);
            }).then((err) => {
                fail(err)
            })
        })
    }
}