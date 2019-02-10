import store from '@/store'

const HEADERS = {
    'Content-Type': 'application/json'
};

export default {
    getSearchResult(query) {
        if (store.state.isAuthenticated) {
            HEADERS['Authorization'] = 'Token ' + store.state.token;
        }
        const apiUrl = 'api/search/?q=' + query;
        const payload = {
            method: 'GET',
            headers: HEADERS
        };
        return fetch(apiUrl, payload).then(response => response.json());
    }
}