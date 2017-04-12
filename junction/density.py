from __future__ import with_statement
import math
import os
import glob
import re

newlist = []
r = []
lll = []
sum = 0
i = 0
junc = 0
j = 3
dist = 0
with open('output.txt') as inputfile:
	results = []
	for line in inputfile:
		l = re.findall(r"[\w]+",line)
		results += l
	newlist = [s for s in results if s.isdigit()]
	while i < (len(newlist)-1):
		sum = sum + int(newlist[i])
		i = i+1
	junc = int(newlist[len(newlist)-1])
inputfile.close()


for filename in glob.glob('input/*.txt'):
	with open(filename) as input1:
		for line in input1:
			lll= (line.strip().split(','))
			r += lll
		while j < (len(r)-4):
			dlong = float(r[j+4]) - float(r[j+1])
			dlat = float(r[j+3]) - float(r[j])
			a = (math.pow((math.sin(dlat/2.0)),2)) + math.cos(float(r[j])) * math.cos(float(r[j+3])) * math.pow((math.sin(dlong/2.0)),2)
			c = 2 * math.atan2(math.sqrt(a),math.sqrt(1-a))
			d = 6371 * c
			j = j+3
			dist = dist + d
	input1.close()
landmark_density = sum/dist
junct_density = junc/dist
print landmark_density, ",",junct_density
out = open('density.txt','w')
print >> out, landmark_density, ',' , junct_density
out.close()
		


		