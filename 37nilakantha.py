def nilakantha(n):
	npi = 3
	for i in range(n):
		bottom = ((2 + (2 * i)) * (3 + (2 * i)) * (4 + (2 * i)) * -((-1) ** i))
		npi = npi - (4 / bottom)
		print(npi)

nilakantha(4)
nilakantha(10)
nilakantha(100)