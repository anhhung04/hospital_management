import requests

username = ""
password = ""
BASE = "http://localhost:8000/api"
def wpath(path): return BASE + path


def login():
    return requests.post(wpath('/auth/login'), json={"username": username, "password": password}).json()['data']['access_token']


_sess = requests.session()
_sess.headers.update({
    'Authorization': f'Bearer {login()}'
})
