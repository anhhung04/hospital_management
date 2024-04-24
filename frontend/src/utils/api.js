function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
  }

function apiCall({ endpoint, method = "GET", requestData,}) {
    const BASE_URL = import.meta.env.VITE_BASE_URL || "";
      const  cookies = getCookie('access_token');
    // console.log(cookies)
    async function fetchData() {
        const res = await fetch(BASE_URL + endpoint, {
            method: method,
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${cookies}`
            },
            body: JSON.stringify(requestData)
        });
        return res.json();
    }

    return fetchData();
}

export default apiCall;
