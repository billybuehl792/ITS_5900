# project8.py - JSON file reading and printing
# prints readable json data in terminal

#import
import requests, sys, json


# JSON data URL
url = 'http://www.its.ohio.edu/kruse/classes/data/contact.json'


# check url
response = requests.get(url)
try:
	response.raise_for_status()
except:
	print('Invalid URL')
	sys.exit()


# collect data
jsonData = json.loads(response.text)


#print fancy data
print('\nData from: ' + url + '\n')
for i in jsonData:
	if isinstance(jsonData[i],list):
		print('\n' + i + ':')
		for p in jsonData[i]:
			for q in p:
				print(q + ':', p[q] + '   ', end='')
			print()
	else:
		print(i + ':   ', jsonData[i])


print('\ndone.')