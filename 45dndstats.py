import random

def roll_d6(n):
	for i in range(n):
		d6 = random.randint(1, 6)
		return d6

def roll_d6r1(n):
	for i in range(n):
		d6 = random.randint(1, 6)
		if d6 == 1: d6 = roll_d6(1)
		return d6

def roll_3d6(n):
	total = 0
	for i in range(n):
		score = 0
		for j in range(3):
			d1 = roll_d6(1)
			d2 = roll_d6(1)
			d3 = roll_d6(1)
			score =+ d1 + d2 + d3
		total += score
	print(total / n)

def roll_3d6r1(n):
	total = 0
	for i in range(n):
		score = 0
		for j in range(3):
			d1 = roll_d6r1(1)
			d2 = roll_d6r1(1)
			d3 = roll_d6r1(1)
			score =+ d1 + d2 + d3
		total += score
	print(total / n)

def roll_3d6x2(n):
	total = 0
	for i in range(n):
		score = 0
		for j in range(3):
			d1 = roll_d6(1)
			d2 = roll_d6(1)
			if d1 > d2:	score += d1
			else: score += d2
		total += score
	print(total / n)

def roll_4d6d1(n):
	total = 0
	for i in range(n):
		score = 0
		d1 = roll_d6(1)
		d2 = roll_d6(1)
		d3 = roll_d6(1)
		d4 = roll_d6(1)
		if d1 <= d2 and d1 <= d3 and d1 <= d4:
			score += d2 + d3 + d4
		elif d2 <= d1 and d2 <= d3 and d2 <= d4:
			score += d1 + d3 + d4
		elif d3 <= d1 and d3 <= d2 and d3 <= d4:
			score += d1 + d2 + d4
		elif d4 <= d2 and d4 <= d3 and d4 <= d1:
			score += d1 + d2 + d3
		total += score
	print(total / n)


roll_3d6(1000)
roll_3d6r1(1000)
roll_3d6x2(1000)
roll_4d6d1(1000)