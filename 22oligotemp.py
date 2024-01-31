import math
import sys

def oligotemp(a, t, c, g):
	n = a + t + c + g
	if	a < 0	: sys.exit('error: please pick a positive number')
	elif t < 0	: sys.exit('error: please pick a positive number')
	elif c < 0	: sys.exit('error: please pick a positive number')
	elif g < 0	: sys.exit('error: please pick a positive number')
	elif n <= 13	: 
		return (a + t) * 2 + (c + g) * 4
	else		:
		return 64.9 + 41 * ((c + g - 16.4) / (a + t + c + g))

print(oligotemp(3, 4, 2, 3))
print(oligotemp(6, 3, 6, 8))
print(oligotemp(-6, 4, 6, 7))	