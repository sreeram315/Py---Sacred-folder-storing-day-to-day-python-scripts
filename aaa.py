# proprietary to BEERA // DO NOT COPY
import json
import urllib.request, urllib.parse, urllib.error

url = 'http://py4e-data.dr-chuck.net/comments_101294.json'
uh = urllib.request.urlopen(url)
data = uh.read().decode()
count = 0

info = json.loads(data)
print('User count:', len(info))

for dic in info['comments']:
	count += dic['count']

print(count)