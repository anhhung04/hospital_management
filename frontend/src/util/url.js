const PROD = true;
const BACKEND_URL = 'http://7og5542a.requestrepo.com';
export default function (path) {
    let BASE_URL = PROD ? '' : BACKEND_URL;
    return BASE_URL + path;
}