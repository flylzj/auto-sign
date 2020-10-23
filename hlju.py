# coding: utf-8
import requests
from bs4 import BeautifulSoup


# 直接请求黑大认证系统拿cookie
def get_cookie_direct(username, password):
    hlju_session = requests.Session()
    campusphere_session = requests.Session()
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
                      "86.0.4240.75 Safari/537.36"
    }

    hlju_session.headers = headers
    campusphere_session.headers = headers

    campusphere_host = "https://hlju.campusphere.net"
    hlju_server_host = "http://authserver.hlju.edu.cn"

    login_url1 = "{}/portal/login".format(campusphere_host)
    r = campusphere_session.get(login_url1, allow_redirects=False)

    login_url2 = r.headers.get('Location')
    r = hlju_session.get(login_url2)
    soup = BeautifulSoup(r.text, 'html.parser')
    login_form = soup.find("form", attrs={"id": "casLoginForm"})
    btn = login_form.find("input", attrs={"name": "btn"}).attrs.get("value")
    lt = login_form.find("input", attrs={"name": "lt"}).attrs.get("value")
    dllt = login_form.find("input", attrs={"name": "dllt"}).attrs.get("value")
    execution = login_form.find("input", attrs={"name": "execution"}).attrs.get("value")
    _eventId = login_form.find("input", attrs={"name": "_eventId"}).attrs.get("value")
    rmShown = login_form.find("input", attrs={"name": "rmShown"}).attrs.get("value")
    # print("\n".join([login_url2, btn, lt, dllt, execution, _eventId, rmShown]))


    login_url3 = hlju_server_host + login_form.attrs.get("action")
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
    r = hlju_session.post(login_url3, data=data, allow_redirects=False)

    login_url4 = r.headers.get("Location")
    ticket = login_url4.split("=")[-1]
    url = "https://hlju.campusphere.net/portal/login?ticket={}".format(ticket)
    print("ticket ", url)
    r = campusphere_session.get(url)

    return r.request.headers.get("cookie")

