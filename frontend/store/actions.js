import * as mutationTypes from './mutations-types'
import pagesApi from '@/services/api-helper/pages'
import contentApi from '@/services/api-helper/contents'
import appConfigApi from '@/services/api-helper/app-configs'

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

    updatePage(context, payload) {
        return new Promise((success, fail) => {
            pagesApi.putPage(payload).then((response) => {
                if (response.path) {
                    success(response);
                }
            }, (error) => {
                fail(error)
            });
        })
    },

    deletePage(context, pageSlug) {
        return new Promise((success, fail) => {
            pagesApi.deletePage(pageSlug).then((response) => {
                if (response.status === 204) {
                    const pageIndex = context.getters.getPageIndexByPath(pageSlug);
                    context.commit(mutationTypes.deletePage, pageIndex);
                    success(response);
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
                success(content);
            }).then((err) => {
                fail(err)
            })
        })
    },

    putPageContent(context, data) {
        return new Promise((success, fail) => {
            contentApi.putContent(data).then((content) => {
                success(content);
            }).then((err) => {
                fail(err)
            })
        })
    },

    deletePageContent(context, contentIdentifier) {
        return new Promise((success, fail) => {
            contentApi.deleteContent(contentIdentifier).then((content) => {
                success(content);
            }).then((err) => {
                fail(err)
            })
        })
    },

    getContentDetailsFromApi(context, slug) {
        return new Promise((success, fail) => {
            contentApi.getContentDetails(slug).then((content) => {
                success(content);
            }).then((err) => {
                fail(err);
            })
        })
    },

    getAppConfigFromApi(context) {
        return new Promise((success, fail) => {
            appConfigApi.getAppConfigs().then((data) => {
                context.commit(mutationTypes.updateAppConfig, data);
                success(data)
            })
        })
    },

    updateAppConfigPostApi(context, data) {
        return new Promise((success, fail) => {
            appConfigApi.postAppConfig(data).then((config) => {
                context.commit(mutationTypes.updateAppConfig, config);
                success(config);
            }).then((err) => {
                fail(err)
            })
        })
    }
}