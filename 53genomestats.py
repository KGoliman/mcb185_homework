import gzip
import sys

gffpath = sys.argv[1]
feature = sys.argv[2]
lengths = []

def mean(vals):
	total = 0
	for val in vals: total += val
	return round((total/len(vals)), ndigits = 0)

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

with gzip.open(gffpath, 'rt') as fp:
	for line in fp:
		words = line.split()
		if words[2] == feature: # repeat for CDS and exon
			beg = int(words[3])
			end = int(words[4])
			vals = end - beg + 1
			lengths.sort
			lengths.append(end - beg + 1)
	print('type', feature, sep = '\t')
	print('length', len(lengths), sep = '\t')
	print('min', lengths[0], sep = '\t')
	print('max', lengths[-1], sep = '\t')
	print('mean', mean(lengths), sep = '\t')
	print('standev', standev(lengths), sep = '\t')
	print('median', median(lengths), sep = '\t')