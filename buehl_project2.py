#!python3
#project2_Buehl.py - regex stuff to find .exe files

import os, sys

#Retrieve vars from command line
if len(sys.argv)>1:
	file = sys.argv[1]
else:
	file = input('Please enter your file\'s location: ')

#Check to see if path seems legit
#while os.path.isfile(file) and file.endswith('.txt') == False:     <-- why wont this work?
#while False and False == False:									<-- or this?
while os.path.isfile(file) == False or file.endswith('.txt') == False:
	file = input('Sorry, I\'m going to need a \'.txt\' file with a REAL file location: ')

#Open file
textFile = open(file, 'r')

#Find .exe files/ add them to exeFiles/ close file
exeFiles = []
for file in list(textFile):
	file = file.strip().lower()
	if file.endswith('.exe'):
		exeFiles.append(file)
	else:
		continue
textFile.close()

#Print searching
print('Searching for \'.exe\' files...\n')

#Print list of .exe files
print(str(len(exeFiles)) + ' \'.exe\' files found in your \'.txt\' file:\n')
if len(exeFiles) > 0:
	for file in exeFiles:
		print(file)

print('\ndone.')