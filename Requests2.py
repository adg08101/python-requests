# Ejercicio Completo de HTTP Verbs
import json

import requests
from requests.auth import HTTPBasicAuth


class MyAdapter(object):
    pass


if __name__ == '__main__':
    s = requests.Session()
    r = requests.Request(
        'GET',
        url='https://api.github.com/repos/kennethreitz/requests/git/commits/a050faf084662f3a352dd1a941f2c7c9f886d4ad'
    )
    preparedRequest=r.prepare()
    response = s.send(preparedRequest)
    if response.status_code == requests.codes.ok:
        if response.headers['content-type'] == 'application/json; charset=utf-8':
            commit_data = response.json()
            print(commit_data[u'committer'], 'is the committer')
            print(commit_data[u'message'], 'is the message')
            verbs = requests.options(r.url)
            print(verbs.headers['access-control-allow-methods'])
            r = requests.get('https://api.github.com/repos/kennethreitz/requests/issues/482')
            issue = json.loads(r.text)
            print(issue[u'title'])
            print(issue[u'comments'])
            r = requests.get(r.url + u'/comments')
            comments = r.json()
            print(comments[0].keys())
            print(comments[2][u'body'])
            print(comments[2][u'user'][u'login'])
            body = json.dumps({u"body": u"Sounds great! I'll get right on it!"})
            url = u"https://api.github.com/repos/kennethreitz/requests/issues/482/comments"
            auth = HTTPBasicAuth('adg08101@gmail.com', 'ContraGH2021-*')
            r = requests.post(url=url, data=body, auth=auth)
            print(r.status_code)
            r = requests.delete(url=url, auth=auth)
            r = requests.head(url=url, auth=auth)
            print('Bye', r.headers['Server'])
            url = 'https://api.github.com/users/kennethreitz/repos?page=1&per_page=10'
            r = requests.head(url=url)
            print(r.links)
            s = requests.Session()
            s.mount('http://www.github.com', MyAdapter())
    else:
        print('Something went wrong')

import ssl

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager


class Ssl3HttpAdapter(HTTPAdapter):
    """"Transport adapter" that allows us to use SSLv3."""

    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(num_pools=connections,
                                       maxsize=maxsize,
                                       block=block,
                                       ssl_version=ssl.PROTOCOL_SSLv3)
