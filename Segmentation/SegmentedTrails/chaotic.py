from __future__ import with_statement
import math
import glob
import os

results = []
r = []
i = 3
j = 3
for filename in os.listdir(os.getcwd()):
	for filename in glob.glob('*.txt'):
		with open(filename) as inputfile:
			for line in inputfile:
				lll= (line.strip().split(','))
				results += lll
for filename2 in glob.glob('F:/wamp/www/Final/Heatmap/heat.txt'):
	with open(filename2) as input:
		for line in input:
			l= (line.strip().split(','))
			r += l
while j < (len(r)-4):
	while i < (len(results)-4):
		if ((results[i] == r[j]) & (results[i+1] == r[j+1])):
			f = open('F:/wamp/www/Final/Segmentation/chaotic.txt','w')
			print >> f, results[i], ',' , results[i+1], ',' , r[j+2]
			print results[i], "," , results[i+1], "," , r[j+2]
		i=i+3
	j=j+3

	

	
			
