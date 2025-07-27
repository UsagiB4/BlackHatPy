import requests
r = requests.get('https://yahoo.com/', allow_redirects=False)
stat = r.status_code
print(stat)
if stat == 200:
    print("OK. Good to go")
    print(r.url)
elif stat == 404:
    print("Opppssss, I couldn't find the content")
    print(r.url)
elif stat == 301:
    print("You are being redirected......")
    f = requests.get(r.url, allow_redirects=True)
    print("location: ", r.url)
    if f.status_code == 200:
        print("you have been redirected successfully")
        print("Location: ", f.url)
    else:
        print(f.status_code)
        print('something went wrong')

