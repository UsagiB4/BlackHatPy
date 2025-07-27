import requests
from requests.utils import DEFAULT_CA_BUNDLE_PATH

'''
To Set Proxy for Burp
===========================
export REQUESTS_CA_BUNDLE="/path/to/pem/encoded/cert"
export HTTP_PROXY="http://127.0.0.1:8080"
export HTTPS_PROXY="http://127.0.0.1:8080"

To unset proxy for burp
++++++++++++++++++++++++++++
unset REQUESTS_CA_BUNDLE
unset HTTP_PROXY
unset HTTPS_PROXY

'''


# get request
r = requests.options('https://api.github.com/events', verify=False)
print(r)

'''
requests.put() === as PUT method
requests.delete() === as DELETE method
request.head() === as HEAD method
request.options() === as OPTIONS method
'''

# Sending data 
dataR = {'hello': 'world', 'whats': 'up'}
dataS = {'new':'world', 'order': [1, 23]}
r = requests.get('https://httpbin.org/get', params=dataR, verify=False)
print(r,'\n', r.url)
r = requests.get('https://httpbin.org/get', params=dataS, verify=False)
print(r,'\n', r.url)


# getting contents

# r = requests.get('https://api.github.com/events')
# r.encoding = 'ISO-8859-1'

# getting contents as text
# conts= r.text
# print(conts)

"""
r.content == will return content into binary mode
r.json() == will return content into json format
r.raw == raw formate
"""

# Adding custom header

url = "https://www.google.com"
headers = {'user-agent': 'hello-from-python/3.12.2'}

req = requests.get(url, headers=headers)
print(req)
