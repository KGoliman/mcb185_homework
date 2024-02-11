import random

def roll_d20(n):
	for i in range(n):
		d20 = random.randint(1, 20)
		return d20

limit = 1000
print('Rolls', 'Success', 'Failure', 'Lucky20', sep = '\t')
tot_success = 0
tot_failure = 0
tot_revive = 0
for i in range(limit):
	success = 0
	failure = 0
	revive = 0
	while success < 3 and failure < 3 and revive != 1:
		d20 =roll_d20(1)
		if d20 == 20:
			revive = 1
			tot_revive += 1
		if d20 < 10 and d20 != 1:
			failure += 1
		if d20 == 1:	failure += 2
		if 9 < d20 < 20:	success += 1
		if success >= 3: tot_success += 1
		if failure >= 3: tot_failure += 1
		
print(
	limit, tot_success/limit, tot_failure/limit, tot_revive/limit, sep = '\t'
	)

