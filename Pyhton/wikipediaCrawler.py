import time
import urllib

import bs4
import requests


start_url = "https://jionetportal.jio.in/"


def find_first_link(url):
    response = requests.get(url)
    html = response.text

while True:
    find_first_link(start_url)
    print(start_url)
    time.sleep(5)
    

    