import sys
import math

def triangular(n):
	if n < 1: sys.exit('error: pick a number more than 0')
	i = 0
	m = 0
	while i != n:
		i = i + 1
		m = m + i
	return m

def factorial(n):
	if n == 0: return 1
	i = 0
	m = 1
	while i != n:
		i = i + 1
		m = m * i
	return m

def euler(n):
	e = 0
	for n in range(n):
		e = e + 1 / factorial(n)
	return e
	
def is_perfect_square(n):
	root = math.sqrt(n)
	if math.isclose(root, root // 1): return True
	return False

def is_prime(n):
	for den in range(2, n//2):
		if n % den == 0: return False
	return True

print(triangular(5))
print(factorial(5))
print(euler(10))
print(is_perfect_square(4))
print(is_prime(3))