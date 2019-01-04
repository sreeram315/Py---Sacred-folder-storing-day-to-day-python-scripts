# proprietary to BEERA // DO NOT COPY
# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def indexed_tag(url,t,n):
	for i in range(t):
		print('going into',url)
		html = urllib.request.urlopen(url, context=ctx).read()
		soup = BeautifulSoup(html, 'html.parser')
		tag = soup('a')[n-1]
		url = tag.get('href', None)
	return tag


url = 'http://py4e-data.dr-chuck.net/known_by_Katharine.html'


# Retrieve all of the anchor tags
print(indexed_tag(url,7,18))
