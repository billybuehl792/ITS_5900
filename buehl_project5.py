#!python3
# buehl_project5.py - redundant calculator 

import math

#stuff that will end the program
quitters = ['quit', 'x', 'q', 'exit']

#print "enter 'quit' to exit calculator"
print('Basic python calculator')
print('Enter x, q, quit, or exit to quit.')

#main loop calculator
while True:
	str = input('>> ')
	if str.lower() in quitters:
		break
	else:
		try:
			if 'log2' in str:
				str = str.replace('log2', 'math.log2')
			elif 'log' in str: 
				str = str.replace('log', 'math.log10')
			elif 'ln' in str:
				str = str.replace('ln', 'math.log')

			calc = eval(str)
			print(calc)
		except NameError:
			print('That character isn\'t allowed. Try again.')
		except ZeroDivisionError:
			print('Can\'t divide by zero. Sorry pal.')
		except:
			print('Please enter a legal calculation.')

# now we're done
print('done.')