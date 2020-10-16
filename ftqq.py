# coding:utf-8
import requests


def msg_to_wechat(SKEY, text):
    msg_host = "https://sc.ftqq.com/{}.send".format(SKEY)
    params = {
        "text": text
    }
    requests.get(msg_host, params=params)


if __name__ == '__main__':
    SKEY = "SCU118498T956fb616f4c0aed098bf95cd187c91cd5f8913afec05b"
    text = "越哥收到我的消息了吗"
    msg_to_wechat(SKEY, text)