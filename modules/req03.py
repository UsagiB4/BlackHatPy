import requests

url = "http://github.com/events/"
cookie = {"biscuit":"chocolaty"}
resp = requests.get(url, cookies=cookie)
print(resp)

cookieJar = requests.cookies.RequestsCookieJar()
cookieJar.set('crunchy', 'biscuit', domain="github.com", path='/events')
r = requests.get(url, cookies=cookieJar)
print(r.cookies.get)
