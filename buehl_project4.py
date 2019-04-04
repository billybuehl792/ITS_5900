#!python3
#project4_buehl.py - merges existing .csv files into one csv file

import os, csv
from operator import itemgetter


#Check to see if paths seems legit (function)
t = 1
def isFile():
	global t
	file = input('Enter .csv' + str(t) + ' file location: ')
	while not (os.path.isfile(file) and file.endswith('.csv')): 
		file = input('Sorry, I\'m going to need a \'.csv\' file with a REAL file location: ')
	t += 1
	return file

# isInt function
def isInt(val):
	try:
		int(val)
		return True
	except ValueError:
		return False



# Retrieve vars from input/ open files/ readers
csv1File = isFile()
csv2File = isFile()
#csv1File = '/Users/BillyBuehl/Dropbox/python_stuff/ITS_5900/project4csv/testInput(1).csv'
#csv2File = '/Users/BillyBuehl/Dropbox/python_stuff/ITS_5900/project4csv/testInput(2).csv'
csv1 = open(csv1File, 'r')
csv2 = open(csv2File, 'r')
csv1Reader = csv.reader(csv1)
csv2Reader = csv.reader(csv2)

#Get column key val
columnKey = input('Enter column key(\'2\' for my samples): ')
while not isInt(columnKey):
	columnKey = input('Enter a number: ')
columnKey = int(columnKey)-1


#add csv2 stuff to a list
csvMatchList = []
csvFileList = []

#csvFile#1 list appending
for line in csv1Reader:
	if line[columnKey] not in csvMatchList:
		csvMatchList.append(line[columnKey])
		csvFileList.append(line)
	else:
		continue

#csvFile#2 list appending
#next(csv2Reader)
for line in csv2Reader:
	if line[columnKey] not in csvMatchList:
		csvMatchList.append(line[columnKey])
		csvFileList.append(line)
	else:
		continue


#create new writefile
writeFile = os.path.dirname(csv1File) + '/mergeFile.csv'
n = 1
while os.path.isfile(writeFile):
	yesOrNo = input(writeFile + ' exists already. Are you sure you want to overwrite? (y/ n):')
	if yesOrNo.lower() == 'y':
		break
	else:
		writeFile = os.path.dirname(csv1File) + '/mergeFile' + str(n) + '.csv'
		n+=1
writeFile1 = open(writeFile, 'w')
writeFileWriter = csv.writer(writeFile1)

#sort and create new csv file
csvFileList.sort(key=itemgetter(columnKey))
for line in csvFileList:
	writeFileWriter.writerow(line)

#close files
csv1.close()
csv2.close()
writeFile1.close()


print('\n' + str(len(csvFileList)) + ' rows written to ' + writeFile)
print('\ndone.')