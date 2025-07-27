import requests

s = requests.Session()

s.get("https://httpbin.org/cookies/set/sessioncookie/121212121")
res = s.get("https://httpbin.org/cookies")

print(res.request.headers)