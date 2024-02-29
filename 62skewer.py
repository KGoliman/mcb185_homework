import dogma
import sys

seq = 'ATCTGGATCGGATCTACTGCATTGCTAGGCT'

w = 4
sw = 1
g = seq[0:w].count('G')
c = seq[0:w].count('C')

for i in range(len(seq) - w + 1):

	off = seq[i]
	on = seq[i+w-1]
	if on == 'G': g += 1
	elif off == 'G': g -= 1

	if on == 'C': c += 1
	elif off == 'C': c -= 1
	comp = (c+g)/w
	
	if (g+c) > 0: skew = (g-c)/(g+c)
	else: skew = 0
	
	print(i, comp, skew)