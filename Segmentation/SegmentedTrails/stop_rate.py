from __future__ import with_statement
import math
import glob
import os


i = 3
vth = 0.02
count = 0
f_line = []
l_line = []
first_line = []
lll = []
for filename in os.listdir(os.getcwd()):
	for filename in glob.glob('*.txt'):
		results = []
		with open(filename) as inputfile:
			for line in inputfile:
				lll= (line.strip().split(','))
				results += lll
		while i < (len(results)-4):
			dlong = float(results[i+4]) - float(results[i+1])
			dlat = float(results[i+3]) - float(results[i])
			a = (math.pow((math.sin(dlat/2.0)),2)) + math.cos(float(results[i])) * math.cos(float(results[i+3])) * math.pow((math.sin(dlong/2.0)),2)
			c = 2 * math.atan2(math.sqrt(a),math.sqrt(1-a))
			d = 6371 * c
			i = i+3
			if d < vth:
				count = count+1
		inputfile.close()
		
		with open(filename) as inputfile:
			for j, line in enumerate(inputfile):
				if j == 1:
					first_line = (line.strip().split(','))
			#f= (first_line.strip().split(','))
			f_line += first_line
			for line in inputfile:
				pass
			last = line
			l= (last.strip().split(','))
			l_line += l
		long = float(l_line[1]) - float(f_line[1])
		lat = float(l_line[0]) - float(f_line[0])
		a1 = (math.pow((math.sin(lat/2)),2)) + math.cos(float(f_line[0])) * math.cos(float(l_line[0])) * math.pow((math.sin(long/2)),2)
		c1 = 2 * math.atan2(math.sqrt(a1),math.sqrt(1-a1))
		d1 = 6371 * c1
		stop_rate = count/d1
print stop_rate
out = open('F:/wamp/www/Final/Segmentation/stop_rate.txt','w')
print >> out , stop_rate
out.close()
			
			