# proprietary to BEERA // DO NOT COPY
# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE



print('3')
url = 'http://py4e-data.dr-chuck.net/comments_101291.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
print('ff')
sum=0
for tag in tags:
    # Look at the parts of a tag
    tag=str(tag)
    lit = re.findall('[0-9]+',tag)
  #  print(lit)
    for i in lit: sum+=int(i)

print(sum)
 
