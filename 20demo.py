#20demo.py by Kobe Goliman
import math
import sys

print('"hello, again"') # greeting

def greeting():
	print('"hello yourself"')

def convertmphtofps(a):
	if a <= 0: sys.exit('error: a must be greater than 0')
	return a * 5280 / 3600

def dnaconcod260(a, b):
	if a <= 0: sys.exit('error: a must be greater than 0')
	if b <= 0: sys.exit('error: b must be greater than 0')
	return 50 * a * b

def converttempctof(a):
	if a <= -273: sys.exit('error: pick a temperature above absoulte zero')
	return 32 + 9/5 * a

def pointdistance(x1, y1, x2, y2):
	return math.sqrt(
	((x2 - x1) ** 2) + ((y2 - y1) ** 2)
	)

def pythagoras(a, b):
	if a <= 0: sys.exit('error: a must be greater than 0')
	if b <= 0: sys.exit('error: b must be greater than 0')
	return math.sqrt(a**2 + b**2)

def midpoint(x1, y1, x2, y2):
	mx = (x1 + x2) / 2
	my = (y1 + y2) / 2
	return mx, my

def isinteger(a):
	if type(a) == int	: return True
	else			: return False
	
def oddnumber(a):
	if a % 2 == 1: return True
	else: return False

def validprob(a):	
	if 0 < a < 1: return True
	else		: return False
	
def dnamweight(a):
	if		a == 'A': return 313.21
	elif	a == 'T': return 304.20
	elif	a == "C": return 289.18
	elif	a == "G": return 329.21
	else		: sys.exit('error, please pick, A, T, C, or G')

def dnacomplement(a):
	if		a == 'A': return 'T'
	elif	a == 'T': return 'A'
	elif	a == "C": return 'G'
	elif	a == "G": return 'C'
	else		: sys.exit('error, please pick, A, T, C, or G')
	

	
greeting()
print(convertmphtofps(60))
print(dnaconcod260(70, 100))
print(converttempctof(-40))
print(pointdistance(2, 4, -3, -5))
print(pythagoras(3, 4))
print(pythagoras(1, 1))
print(midpoint(-4, -6, 7, 8))
print(isinteger('integer'))
print(oddnumber(-10))
print(validprob(0.1))
print(dnamweight('A'))
print(dnacomplement('T'))