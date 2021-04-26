import json
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

def main(start, end):
    url_start = 'http://127.0.0.1:8000/11/'
    url_end = '/bla-bla-bla/results'
    # response = requests.get(url)
    i = int(start)
    while i <= int(end):
        url = url_start + str(i) + url_end
        try:
            response = requests.get(url)
            print('GET', url, 'response:', response)
        except requests.exceptions.ConnectionError:
            response = 'Connection error'
            print('GET', url, 'response:', response)
        # print('GET', url, 'response:', response)
        i += 1

    # print(start, end)
    # print(response)

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
    args = sys.argv
    main(args[1], args[2])
