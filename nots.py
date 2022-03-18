# proprietary to BEERA // DO NOT COPY
import os
from urllib.request import urlopen
from bs4 import BeautifulSoup
from time import sleep

def notify(title, text, sound_name = 'al'):
    os.system("""
              osascript -e 'display notification "{}" with title "{}" sound name "{}"'
              """.format(text, title, sound_name))



#notify("Title", "Heres an alert")
print('1')

disconnected = True
while (True):
	try:
		url = 'http://jiofi.local.html/'
		html = urlopen(url).read()
		soup = BeautifulSoup(html, "html.parser")


		battery_tag = soup.find("input", {"id": "batterylevel"})
		battery_level = (int(str(battery_tag['value'])[:-1]))

		cation = f"JioFi Battery at {battery_level}%"
		# if battery_level < 20:
		# 	cation = f"JioFi Battery CRITICAL at {battery_level}%"
		if disconnected:
			cation = f"Connected to INDRIYVIJAY\n" + cation
			disconnected = False
		notify(f"JioFI Battery",cation)
		if(battery_level < 100):
			delay = 600
		if(battery_level < 50):
			delay = 400
		if(battery_level < 30):
			delay = 250
		if(battery_level < 20):
			delay = 100
		if(battery_level < 5):
			delay = 10
		print('delay = ',delay)
		for _ in range(delay):
			sleep(1)
			print('7', _)
			urlopen(url).read()
	except:
		print('ERRORED')
		sleep(1)
		if not disconnected:
			notify(f"JioFI Battery", f"Disconnected from INDRIYVIJAY\n at battery level: {battery_level}%")
		disconnected = True
		pass




