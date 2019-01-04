# proprietary to BEERA // DO NOT COPY
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter Location:')
print('Retrieving',url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrived',len(data.decode()))
tree = ET.fromstring(data)

counts = tree.findall('comments/comment')
ans = 0
c = 0
for item in counts:
	c += 1
	ans += int(item.find('count').text)
print('count:',c)
print('sum:',ans)
