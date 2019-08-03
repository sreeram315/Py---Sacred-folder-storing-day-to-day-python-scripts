from os import listdir
from os.path import isfile, join
import os


# onlyfiles = [f for f in listdir('‎⁨gvjhb') if isfile(join(‎⁨gvjhb, f))]

photos = os.listdir('/Users/sreerammaram/Desktop/iasbkndas')

handle = open('sanju_photos2.txt', 'w+')

for name in photos:
	handle.write(name + '\n')

handle.close()
