# proprietary to BEERA // DO NOT COPY
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import ssl
import re
from time import sleep
from bs4 import BeautifulSoup


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


if __name__ == '__main__':
	login_page		=	'https://www.linkedin.com/uas/login?_l=en'
	
	options 		= webdriver.ChromeOptions()
	#options.add_argument("headless")
	#driver = webdriver.Chrome('C:\\chromedriver.exe', chrome_options = options)
	driver 			= webdriver.Chrome('/Users/sreerammaram/Downloads/chromedriver')
	driver.get(login_page)
	actions = ActionChains(driver)

	email_field = driver.find_element_by_id('session_key-login')
	password_field = driver.find_element_by_id('session_password-login')
	email_field.send_keys('sreerammaram2@gmail.com')
	password_field.send_keys('aditihydari1@')
	driver.find_element_by_id('btn-primary').click()


	upload_image	=	driver.find_element_by_id('ember1044-upload-photo')
	upload_image.send_keys('/Users/sreerammaram/Downloads/aa.jpeg')
	sleep(2)
	
	#sleep(2)
	message_box		=	driver.find_element_by_class_name('mentions-texteditor__content')
	message_box.click()
	actions.send_keys('This is a message')
	actions.perform()
	post_but		=	driver.find_element_by_class_name('button-primary-medium sharing-subaction-bar__post-button sharing-share-box__post-button  post ember-view')
	# sleep(1)
	# #soup 		=	BeautifulSoup(driver.page_source, "html.parser")
	# ids	=	[i for i in re.findall(r'\b\w+\b', driver.page_source) if i.startswith('ember')]
	# print(ids)

	post_but.click()


	
	

	