import asyncio
import json
from asyncio import wait
from fileinput import filename

import requests, sys

"""
# Search GitHub's repositories for requests
response = requests.get(
    'https://api.github.com/search/repositories',
    params=[('q', ['user:adg08101'])],
    headers={'Accept': 'application/vnd.github.v3.text-match+json'},
)

print(response.url)

# Inspect some attributes of the `requests` repository
json_response = response.json()
repository = json_response['items']
for repo in repository:
    print(f'Repository name: {repo["name"]}')  # Python 3.6+
    print(f'Repository language: {repo["language"]}')  # Python 3.6+
    print(f'Repository description: {repo["description"]}\n')  # Python 3.6+
"""
"""
r = requests.post("http://httpbin.org/post")
print(r.text)
"""
"""
import json
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
headers = {'content-type': 'application/txt'}

r = requests.post(url, data=json.dumps(payload), headers=headers)

print(r.json()['message'])
"""
"""def jason():
    v = [{
        'id': '100',
        'name': 'MVP 2021',
        'releaseDate': '2021-04-06',
        'reviewScore': '52',
        'category': 'Sports',
        'rating': 'AE'
    }, {
        'id': '101',
        'name': 'MVP 2022',
        'releaseDate': '2021-04-06',
        'reviewScore': '52',
        'category': 'Sports',
        'rating': 'AE'
    }]
    for i in v:
        return i"""

# v = json.loads(json.dumps(v))

"""response = requests.post(url= url, json= jason())
print(response.text)

response = requests.get(url,
                        headers={'Accept': 'application/json'})

obj = response.json()
gid = None

for r in obj:
    if r['name'] == 'MVP 2021':
        gid = r['id']

v = {
  'id': '100',
  'name': 'MVP 2021',
  'releaseDate': '2021-04-06',
  'reviewScore': '100',
  'category': 'Sports',
  'rating': 'AE'
}

response = requests.put(url= url + str(gid), json= v)

response = requests.get(url + str(gid),
                        headers={'Accept': 'application/json'})

print(response.json())

response = requests.delete(url= url + str(gid))
print(response.text)"""


async def main():
    for i in range(100):
        response = requests.get(
            'https://www.tuenvio.cu/lahabana/Products?depPid=46095',
            # params=[('q', ['user:adg08101'])],
            headers={'Accept': 'application/json, text/plain, */*',
                     'Referer': '',
                     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'},
        )
        print(i, response, response.__sizeof__())
        # await asyncio.sleep(3)


""" url_start = 'http://127.0.0.1:8000/11/'
    url_end = '/bla-bla-bla/results'
    # response = requests.get(url)
    i = int(start)
    success = 0
    success_list= []
    fail = 0
    fail_list = []
    while i <= int(end):
        url = url_start + str(i) + url_end
        try:
            response = requests.get(url)
            print('GET', url, 'response:', response, "SUCCESS" if response.status_code == 200 else "FAIL")
            if response.status_code == 200:
                success += True
                success_list.append(i)
            else:
                fail += True
                fail_list.append(i)
        except requests.exceptions.ConnectionError:
            response = 'Connection error'
            print('GET', url, 'response:', response)
        # print('GET', url, 'response:', response)
        i += 1

    print("SUCCEDED:", success, "FAILS:", fail)

    menu(success, success_list, fail, fail_list)


def menu(s, sl, f, fl):
    option = input("Show success = 1\nShow fails = 2\nExit = 3\nSelect Option [1 | 2 | 3]:")
    if option == '1':
        print("Secceded for:")
        print(sl)
        menu(s, sl, f, fl)
    elif option == '2':
        print("Failed for:")
        print(fl)
        menu(s, sl, f, fl)
    else:
        print("Bye")"""

"""print(jason())"""

"""url = 'http://httpbin.org/post'
files = {'file': open('response.txt', 'rb')}

r = requests.post(url, files=files)
print(r.headers)
print(r.cookies)"""

"""response =  requests.get('http://www.github.com', allow_redirects= False, timeout= 1 * 2 / 3)
print(response.url)
print(response.history)"""

if __name__ == '__main__':
    asyncio.run(main())
    """args = sys.argv
    main(args[1], args[2])"""
