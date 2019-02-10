export default {
    getPages(state) {
        return state.pages;
    },
    getPageByPath: (state) => (path) => {
        return state.pages.find(page => page.path === path)
    },
    getCurrentPage(state) {
        return state.currentPage
    },
    getPageIndexByPath: (state) => (path) => {
        return state.pages.findIndex(item => item.path === path)
    },
    getContentByIdentifier: (state) => (hash) => {
        return state.currentPage.contents.find(content => content.identifier === hash)
    },
}