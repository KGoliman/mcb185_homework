import gzip
import sys

gffpath = sys.argv[1]
feature = sys.argv[2]
lengths = []

def mean(vals):
	total = 0
	for val in vals: total += val
	return (total/len(vals))

def standev(vals):
	total = 0
	stdvmn = mean(vals)
	for val in vals: total += ((val - stdvmn) ** 2)
	return round(((total / len(vals))**0.5), ndigits = 0)

def median(vals):
	vals.sort()
	midx1 = vals[len(vals) // 2]
	midx2 = vals[(len(vals) // 2) - 1]
	if len(vals) % 2 == 1: med = midx1
	else: med = (midx1 + midx2) / 2
	return med

def minmax(vals):
	mini = vals[0]
	maxi = vals[0]
	for val in vals:
		if val < mini: mini = val
		if val > maxi: maxi = val
	return mini, maxi
	
with gzip.open(gffpath, 'rt') as fp:
	for line in fp:
		words = line.split()
		if words[2] == feature: # repeat for CDS and exon
			beg = int(words[3])
			end = int(words[4])
			vals = end - beg + 1
			lengths.append(end - beg + 1)
	lengths.sort()

	print('type', feature)
	print('length', len(lengths))
	print('min', 'max', minmax(lengths))
	print('mean', mean(lengths))
	print('standev', standev(lengths))
	print('median', median(lengths))