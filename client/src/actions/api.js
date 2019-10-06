import axios from 'axios';

export const getResults = async (userObj) => {
    const config = { headers: {'Content-Type': 'application/json' }}
    const body = JSON.stringify(userObj);
    try {
        let res = await axios.post('/titanic', config, body);
        return res;
    } catch(err) {
        console.error(err.message);
    }
}