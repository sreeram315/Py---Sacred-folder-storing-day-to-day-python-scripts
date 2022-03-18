from bs4 import BeautifulSoup

# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

import sys
sys.stdout = open('output.txt', 'a')
soup = BeautifulSoup(open('input.txt', 'r').read(), 'html.parser')
string = ''

rows = soup.find_all('tr')

for row in rows[1:]:
	soup_row = BeautifulSoup(str(row), 'html.parser')
	tds = soup_row.find_all('td')
	if not ((tds[2].text).strip()).startswith("CS"): continue
	for t in tds[1:]:
		print((t.text).strip(), end = '   ')
	print("NIT Calicut", end = '')
	print('')