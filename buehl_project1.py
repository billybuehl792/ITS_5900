#! python3
# project1_Buehl.py - Calculates file transfer time

def isFloat(speed):
	try:
		float(speed)
		return True
	except ValueError:
		return False

#Collect file size in Megabytes
size = input('Enter size of file in Megabytes: ')
while isFloat(size) == False:
	size = input('Enter a number: ')

#Collect speed in Mbps
speed = input('Enter estimated transfer speed in Megabits/second: ')
while isFloat(speed) == False:
	speed = input('Enter a number: ')

#calculate times
timeDec = (float(size)*8)/float(speed)

#print outputs
if timeDec >= 60:
	print('Estimated time of transfer: ' + str(timeDec/60) + ' minutes')
else: 
	print('Estimated time of transfer : ' +str(timeDec) + ' seconds')

print('\ndone.')