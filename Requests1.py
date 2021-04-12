import json

import requests
from requests import Request, Session
from requests.auth import AuthBase

"""s = requests.Session()
s.auth = ('user', 'pass')
s.headers.update({'x-testing': 'true'})

# se envían ambos: 'x-test' y 'x-test2'
s.headers['x-testing_again'] = 'true'
s.get('http://www.cubadebate.cu')

print(s.headers)"""

"""s = Session()

data = {
    'head': 'hunter'
}

url = 'http://www.cubadebate.cu'

re = Request(
    'GET',
    data= data,
    url= url
)

req= s.prepare_request(re)

req1 = requests.get('https://www.github.com', verify= True)
print(req1, '-->', 'GitHub')

response= s.send(req)

print(response.headers)"""

"""tarball_url = 'https://download.apkpure.com/b/APK/Y29tLm1pbW9zLmN1dC50aGVncmFzc18xNl9hZTZkZDQ1OQ?_fn=Q3V0IHRoZSBHcmFzc192MS42LjNfYXBrcHVyZS5jb20uYXBr&as=536e1432712af78504cec8b77e50df2c606d2749&ai=-1030371109&at=1617766097&_sa=ai%2Cat&k=5fa3dba037863c90c28daa49c0dcc9d3606fc9d1&_p=Y29tLm1pbW9zLmN1dC50aGVncmFzcw&c=2%7CGAME_SIMULATION%7CZGV2PU1vdXNlJTIwR2FtZXMmdD1hcGsmcz0yNjY4OTkzNCZ2bj0xLjYuMyZ2Yz0xNg'
r = requests.get(tarball_url, stream=True)
print(int(r.headers['Content-length']) / 1000000)"""

"""class PizzaAuth(AuthBase):
    def __init__(self, username):
        self.username=username
    def __call__(self, r, *args, **kwargs):
        r.headers['PizzaAuth']=self.username
        return r
    def __repr__(self):
        return self.username

def hello(s):
    print('All good')

session = Session()
request = Request(
    'GET',
    url='http://localhost:8080/app/videogames',
    hooks=dict(response=hello(session)),
    auth=PizzaAuth('adg08101')
)
req=request.prepare()
response=session.send(req)
print(request.auth)
print(response.text)"""

"""def getProxies():
    return {
        'http': 'http://127.0.0.1:8080',
        'https': 'http://127.0.0.1:3128'
    }


response = requests.get('http://localhost:8080/app/videogames', stream=True, proxies=getProxies())
for l in response.iter_lines():
    print(l)
    print(response.request.hooks)"""

verbs = requests.options('http://www.cubadebate.cu')
print(verbs.headers['Allow'])
# GET,HEAD,POST,OPTIONS

r = requests.get('https://api.github.com/repos/kennethreitz/requests/issues/482')
r.status_code
# 200
issue = json.loads(r.text)
print(issue[u'title'])
# Feature any http verb in docs
print(issue[u'comments'])
# 3