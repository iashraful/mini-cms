const HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': 'Token ' + localStorage.getItem('token')
};

export default {
    getPages() {
        const apiUrl = 'api/pages/';
        const payload = {
            method: 'GET',
            headers: HEADERS
        };
        return fetch(apiUrl, payload).then(response => {response.json()});
    }
}