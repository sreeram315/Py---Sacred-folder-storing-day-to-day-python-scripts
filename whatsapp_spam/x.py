from selenium import webdriver
import urllib.request, urllib.parse, urllib.error
import ssl
from time import sleep
from selenium.webdriver.common.keys import Keys

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


options = webdriver.ChromeOptions()	
driver = webdriver.Chrome('/Users/sreerammaram/Downloads/chromedriver', chrome_options = options)

def main():
	driver.get('http://web.whatsapp.com')
	sleep(12)
	el = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
	count = 0
	nw = 0
	f = open("t.txt", "r")
	for x in f.readlines():
		for word in x.split():
			nw += 1
			print(word, nw)
			# el.send_keys(word)
			el.send_keys("I love you.")
			el.send_keys(Keys.RETURN)
		count += 1
		if(count==124): break
	
	print("Done")


main()

