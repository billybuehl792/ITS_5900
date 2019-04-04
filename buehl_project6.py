#! buehl_project6.py - find website status codes

import urllib3

#disable annoying stuff
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#stuff that will end the program
quitters = ('x', 'q')

#print "enter 'quit' to exit url status finder"
print('Find out now if a website is real!')
print('(Enter x to quit)\n')

#main loop url status finder
http = urllib3.PoolManager()
while True:
	address = input('Enter a URL: ')
	if address in quitters:
		break
	try:
		r = http.request('GET', address, redirect=False);
		print('Status Code: ' + str(r.status))
		input('\n(More Info)\n')
		print(str(r.info()) + '\n')
	except urllib3.exceptions.NewConnectionError:
		print('New Connection Error. Not a real site.')
	except:
		print('Enter legitiment URL')
		
print('\ndone.')