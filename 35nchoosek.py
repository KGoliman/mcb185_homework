def factorial(n):
	if n == 0: return 1
	i = 0
	m = 1
	while i != n:
		i = i + 1
		m = m * i
	return m

def nchoosek(n, k):
	c = factorial(n) / (factorial(k) * factorial(n - k))
	return c

print(nchoosek(10, 4))
print(nchoosek(21, 1))