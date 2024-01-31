import math
import sys

def accuracyf1(tp, tn, fp, fn):
	if	tp < 0: sys.exit('error: tp cannot be a negative number')
	elif	tn < 0: sys.exit('error: tn cannot be a negative number')
	elif	fp < 0: sys.exit('error: fp cannot be a negative number')
	elif	fn < 0: sys.exit('error: fn cannot be a negative number')
	else:
		precision	= tp / (tp + fp)
		recall 		= tp / (tp + fn)
		accuracy	= (tp + tn) / (tp + fp + tn + fn)
		f1		= 2 * ((precision * recall) / (precision + recall))
		return accuracy, f1

print(accuracyf1(4, 5, 6, 7))
print(accuracyf1(8, 5, 6, 3))
print(accuracyf1(9, -2, 4, 5))