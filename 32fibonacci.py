
def fibonacci(n):
	i = 1
	a = -1
	b =  1
	while i < n:
		i = i + 1
		c = a + b
		print(c)
		a = b
		b = c

fibonacci(1)
fibonacci(2)
fibonacci(3)
fibonacci(4)
fibonacci(10)