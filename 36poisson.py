import math

def factorial(n):
	if n == 0: return 1
	i = 0
	m = 1
	while i != n:
		i = i + 1
		m = m * i
	return m

def poisson(n, k):
	c = (math.pow(n, k) * math.pow(math.e, -n)) / factorial(k)
	return c
	
print(poisson(5, 4))
print(poisson(6, 7))