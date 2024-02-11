import random
nts = 'ACGT'

def randnarange(n):
	for i in range(n):
		print('>seq-', i + 1, sep = "")
		for j in range(random.randint(40, 71)):
			print(random.choice(nts), end='')
		print()

randnarange(4)