from __future__ import with_statement
import math
import glob
import os
import csv

results1 = []
results2 = []
results3 = []

i = 0

path1 = 'F:/wamp/www/Final/Segmentation/stop_rate.txt'
path2 = 'F:/wamp/www/Final/junction/density.txt'
path3 = 'F:/wamp/www/Final/Segmentation/chaotic.txt'

if os.path.isfile(path1):
	for filename1 in glob.glob(path1):
		with open(filename1) as inputfile1:
			for line in inputfile1:
				results1= (line.strip())
				print results1

if os.path.isfile(path2):
	for filename2 in glob.glob(path2):
		with open(filename2) as inputfile2:
			for line in inputfile2:
				results2= (line.strip())
				print results2

if os.path.isfile(path3):
	for filename3 in glob.glob(path3):
		with open(filename3) as inputfile3:
			for line in inputfile3:
				results3= (line.strip())

with open('F:/wamp/www/Final/final.csv','wb') as csvfile:
	spamwriter = csv.writer(csvfile,delimiter=' ',quotechar='|',quoting=csv.QUOTE_MINIMAL)
	#if (len(results1) == len(results2)):
	while(i < len(results1)):
		spamwriter.writerow([results1[i]] + [results2[i]])
		i = i + 1





				