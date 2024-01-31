import math
import sys

def quadratic_2intercept(a, b, c):
	n = math.pow(b, 2) - 4 * (a * c)
	if	a == 0	: sys.exit('error: this is not a quadratic function')
	elif	n < 0	: sys.exit('error: there are no real solution')
	elif	n == 0	: sys.exit('error: there are only one x-intercept')
	else		: 
		y = (-b + math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
		z = (-b - math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
	return y, z

print(quadratic_2intercept(2, 20, 10)) 	# 2 x-intercepts
print(quadratic_2intercept(2, 4, 2))	# 1 x-intercept
print(quadratic_2intercept(1, 3, 4))	# 0 x-intercept