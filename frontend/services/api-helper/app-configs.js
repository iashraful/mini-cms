import store from '@/store'

const HEADERS = {
    'Content-Type': 'application/json'
};

export default {
    getAppConfigs(slug) {
        if (store.state.isAuthenticated) {
            HEADERS['Authorization'] = 'Token ' + store.state.token;
        }
        const apiUrl = 'api/app-config/';
        const payload = {
            method: 'GET',
            headers: HEADERS
        };
        return fetch(apiUrl, payload).then(response => response.json());
    },

    postAppConfig(data) {
        if (store.state.isAuthenticated) {
            HEADERS['Authorization'] = 'Token ' + store.state.token;
        }
        const apiUrl = 'api/app-config/';
        const payload = {
            method: 'POST',
            body: JSON.stringify(data),
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
    }
}