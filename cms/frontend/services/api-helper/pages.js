import store from "cms/frontend/store";

const HEADERS = {
    'Content-Type': 'application/json'
};

export default {
    getPages() {
        if (store.state.isAuthenticated) {
            HEADERS['Authorization'] = 'Token ' + store.state.token;
        }
        const apiUrl = 'api/pages/';
        const payload = {
            method: 'GET',
            headers: HEADERS
        };
        return fetch(apiUrl, payload).then(response => response.json());
    },

    postPage(data) {
        if (store.state.isAuthenticated) {
            HEADERS['Authorization'] = 'Token ' + store.state.token;
        }
        const apiUrl = 'api/pages/';
        const payload = {
            method: 'POST',
            body: JSON.stringify(data),
            headers: HEADERS
        };
        return fetch(apiUrl, payload).then((response) => {
            let json = response.json();
            if (response.status === 201) {
                return json;
            } else {
                return json.then(Promise.reject.bind(Promise));
            }
        });
    },

    putPage(data) {
        if (store.state.isAuthenticated) {
            HEADERS['Authorization'] = 'Token ' + store.state.token;
        }
        const apiUrl = 'api/pages/' + data.pageSlug + '/';
        const payload = {
            method: 'PUT',
            body: JSON.stringify(data.page),
            headers: HEADERS
        };
        return fetch(apiUrl, payload).then((response) => {
            let json = response.json();
            if (response.status === 200) {
                return json;
            } else {
                return json.then(Promise.reject.bind(Promise));
            }
        });
    },

    deletePage(pageSlug) {
        if (store.state.isAuthenticated) {
            HEADERS['Authorization'] = 'Token ' + store.state.token;
        }
        const apiUrl = 'api/pages/' + pageSlug + '/';
        const payload = {
            method: 'DELETE',
            headers: HEADERS
        };
        return fetch(apiUrl, payload).then((response) => {
            // let json = response.json();
            if (response.status === 204) {
                return response;
            } else {
                return response.then(Promise.reject.bind(Promise));
            }
        });
    },

    getPageDetails(path) {
        if (store.state.isAuthenticated) {
            HEADERS['Authorization'] = 'Token ' + store.state.token;
        }
        const apiUrl = 'api/pages/' + path + '/';
        const payload = {
            method: 'GET',
            headers: HEADERS
        };
        return fetch(apiUrl, payload).then(response => response.json());
    }
}