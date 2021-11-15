import requests

def login():
    # url = "http://127.0.0.1:8010/eoffice10/server/public/api/auth/login"
    url = "https://www.baidu.com"
    res = requests.get(url)
    print(res.text)


login()


