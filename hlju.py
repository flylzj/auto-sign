# coding: utf-8
import requests
from bs4 import BeautifulSoup


# 直接请求黑大认证系统拿cookie
def get_cookie_direct(username, password):
    session = requests.Session()
    # session.proxies = {"http": "http://127.0.0.1:8080"}
    session.headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
                      "86.0.4240.75 Safari/537.36"
    }
    server_host = "http://authserver.hlju.edu.cn"
    login_url1 = "{}/authserver/login?service=https%3A%2F%2Fhlju.cpdaily.com%2Fportal%2Flogin".format(server_host)

    r = session.get(login_url1)
    soup = BeautifulSoup(r.text, 'html.parser')
    login_form = soup.find("form", attrs={"id": "casLoginForm"})

    login_url2 = server_host + login_form.attrs.get("action")
    btn = login_form.find("input", attrs={"name": "btn"}).attrs.get("value")
    lt = login_form.find("input", attrs={"name": "lt"}).attrs.get("value")
    dllt = login_form.find("input", attrs={"name": "dllt"}).attrs.get("value")
    execution = login_form.find("input", attrs={"name": "execution"}).attrs.get("value")
    _eventId = login_form.find("input", attrs={"name": "_eventId"}).attrs.get("value")
    rmShown = login_form.find("input", attrs={"name": "rmShown"}).attrs.get("value")
    # print("\n".join([login_url2, btn, lt, dllt, execution, _eventId, rmShown]))
    data = {
        "username": username,
        "password": password,
        "btn": btn,
        "lt": lt,
        "dllt": dllt,
        "execution": execution,
        "_eventId": _eventId,
        "rmShown": rmShown
    }
    r = session.post(login_url2, data=data, allow_redirects=False)

    cpdaily_url = r.headers.get("Location")

    cpdaily_session = requests.Session()

    r = cpdaily_session.get(cpdaily_url)

    return r.request.headers.get("cookie")

