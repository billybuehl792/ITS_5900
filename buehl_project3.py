#!python3
#project3_Buehl.py - finds desired file types in a directory

import sys, os


#retrieve vars from command line/ or prompt for input
if len(sys.argv)>2:
	dir = sys.argv[1]
	ext = sys.argv[2]
elif len(sys.argv)>1:
	dir = sys.argv[1]
	ext = input('Enter extension of desired file:')
else:
	dir = input('Please enter a directory:')
	ext = input('Enter extension of desired file:')


#check to see if path seems legit
while os.path.isdir(dir) == False:
	print('Sorry, that\'s not a directory. Please enter a directory path')
	dir = input()

#add .endswith files to a separate list
extFiles = []
for file in os.listdir(dir):
	if file.endswith(ext):
		extFiles.append(file)
	else:
		continue

#print list of exe files
print('\n' + str(len(extFiles)) + ' \'' + ext + '\' files found in your directory')
if len(extFiles) > 0:
	for file in extFiles:
		print(file)

print('\ndone.')