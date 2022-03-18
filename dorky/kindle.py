from bs4 import BeautifulSoup

# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
import sys
sys.stdout = open('output.txt', 'a+')
soup = BeautifulSoup(open('input.txt', 'r').read(), 'html.parser')
string = ''
tags = soup.find_all()
for tag in tags:
	string += f' {str(tag.text)}'

print(string)