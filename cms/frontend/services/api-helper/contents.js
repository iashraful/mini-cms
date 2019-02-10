import store from '@/store'

const HEADERS = {
    'Content-Type': 'application/json'
};

export default {
    getContentDetails(slug) {
        if (store.state.isAuthenticated) {
            HEADERS['Authorization'] = 'Token ' + store.state.token;
        }
        const apiUrl = 'api/contents/' + slug + '/';
        const payload = {
            method: 'GET',
            headers: HEADERS
        };
        return fetch(apiUrl, payload).then(response => response.json());
    },
    postContent(data) {
        if (store.state.isAuthenticated) {
            HEADERS['Authorization'] = 'Token ' + store.state.token;
        }
        const apiUrl = 'api/create-content/';
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

    putContent(data) {
        if (store.state.isAuthenticated) {
            HEADERS['Authorization'] = 'Token ' + store.state.token;
        }
        const apiUrl = 'api/contents/' + data.slug + '/';
        const payload = {
            method: 'PUT',
            body: JSON.stringify(data.data),
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

    deleteContent(identifier) {
        if (store.state.isAuthenticated) {
            HEADERS['Authorization'] = 'Token ' + store.state.token;
        }
        const apiUrl = 'api/contents/' + identifier + '/';
        const payload = {
            method: 'DELETE',
            headers: HEADERS
        };
        return fetch(apiUrl, payload).then((response) => {
            if (response.status === 204) {
                return response;
            } else {
                return response.then(Promise.reject.bind(Promise));
            }
        });
    },
}