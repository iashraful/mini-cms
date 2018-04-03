import * as mutationTypes from "@/store/mutations-types";
import axios from 'axios'
import store from '@/store/index'

export default {
    [mutationTypes.syncMenuItems](state, data) {
        const url = 'api/all-menus/';
        const payload = {
            headers: {
                'Content-Type': 'application/json',
                // Still I am catching the token on fly from local storage
                'Authorization': 'Token ' + store.state.token
            }
        };
        axios.post(url, data, payload).then((response) => {
            if (response.data) {
                console.log(response.data)
            }

        }).catch((err) => {
            console.error(err);
        });
    }
}