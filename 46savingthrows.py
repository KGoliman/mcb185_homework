import random

def roll_d20(n):
	for i in range(n):
		d20 = random.randint(1, 20)
		return d20

def disadvantage_d20(n):
	for i in range(n):
		d1 = random.randint(1, 20)
		d2 = random.randint(1, 20)
		if d1 <= d2: return d1
		else: return d2

def advantage_d20(n):
	for i in range(n):
		d1 = random.randint(1, 20)
		d2 = random.randint(1, 20)
		if d1 >= d2: return d1
		else: return d2

print('DC', 'norm', 'adv', 'dis', sep= '\t')

limit = 1000

for dc in range(5, 16, 5):
	n = 0
	a = 0
	d = 0
	for i in range(limit):
		normal = roll_d20(1)
		advantage = advantage_d20(1)
		disadvantage = disadvantage_d20(1)
		if normal >= dc: n += 1
		if advantage >= dc: a += 1
		if disadvantage >= dc: d += 1
	print(dc, n / limit, a / limit, d / limit, sep= '\t')

