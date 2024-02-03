import math

def is_perfect_square(n):
	root = math.sqrt(n)
	if math.isclose(root, root // 1): return True
	return False
	
def triples(n):
	for a in range(1, n):
		for b in range(1, n):
			if is_perfect_square(a ** 2 + b ** 2) and a < b:
				print(a, b, int(math.sqrt(a ** 2 + b ** 2)))

triples(100)