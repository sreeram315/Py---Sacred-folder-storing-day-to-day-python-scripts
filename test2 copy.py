from bs4 import BeautifulSoup
import requests
import urllib.request, urllib.parse, urllib.error
import ssl
import re
from selenium import webdriver
from time import sleep


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = str(open('html.txt').readlines())

soup = BeautifulSoup(html, 'html.parser')


table = soup.select("table[id=chapterListTable]")[0]

conts = table.select('tr')
links = []
for ex in conts[1:21]:
	link = 'http://bni-gurgaon.in/en-IN/' + ex.find_all('a')[0]['href']
	# print(a['href'])
	name = ex.text[60:-172]
	if name[-1] == '\\': name = name[:-1]
	if name[-2] == '\\': name = name[:-2]
	if name[-3] == '\\': name = name[:-3]
	if name[-4] == '\\': name = name[:-4]
	# print(f'{name} - {link}')
	links.append(link)




def get_html(link):
	options = webdriver.ChromeOptions()
	options.add_argument("headless")
	# driver = webdriver.Chrome('C:\\chromedriver.exe', chrome_options = options)
	driver = webdriver.Chrome('/Users/sreerammaram/Downloads/chromedriver', chrome_options = options)

	driver.get(link)
	sleep(3)
	body = driver.page_source
	driver.close()
	return body


people = []
print(len(links))

count = 0
for link in links:
	html = get_html(link)
	soup = BeautifulSoup(html, 'html.parser')
	table = soup.select("table[id=chapterListTable]")[0]
	conts = table.select('tr')
	
	for ex in conts[2:]:
		arr = ex.text.split('\n')
		l = 'http://bni-gurgaon.in/en-IN/' + ex.find_all('a')[0]['href']
		# print(arr)
		name = arr[1]
		company = arr[2]
		path = arr[3]
		contact = arr[4]
		l = l
		people.append(
			{	
				"name" : name,
				"company": company,
				"path" : path,
				"contact" : contact,
				"link": l
			
			}

			)
	
	count += 1
	print(count)


print(people)









# html = urllib.request.urlopen('http://bni-gurgaon.in/en-IN/chapterdetail?chapterId=rPT9sF7wJ7zdAjaogXrtxQ%3D%3D&name=BNI+Abundance', context=ctx).read()

# # print(html)
# soup = BeautifulSoup(str(open('html2.txt').readlines()), 'html.parser')


# table = soup.select("table[id=chapterListTable]")[0]

# conts = table.select('tr')
# # links = []
# for ex in conts[2:20]:
# 	print(ex)
# 	link = 'http://bni-gurgaon.in/en-IN/' + ex.find_all('a')[0]['href']
# 	# print(a['href'])
# 	name = ex.text[60:-172]
# 	if name[-1] == '\\': name = name[:-1]
# 	if name[-2] == '\\': name = name[:-2]
# 	if name[-3] == '\\': name = name[:-3]
# 	if name[-4] == '\\': name = name[:-4]
# 	print(f'{name} - {link}')
# 	exit()



	



# print((conts[1].select('href')))






















