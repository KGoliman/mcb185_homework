import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])
total = 0

def birthdays(people):
	birthday = []
	for i in range(people):
		d = random.randint(0, days - 1)
		birthday.append(d)
	return birthday

def dup_date(lst):
	lst.sort()
	i = lst[0:]
	j = lst[1:]
	for x, y in zip(i, j):
		if x == y: return True

for i in range(trials):
	group = birthdays(people)
	dupes = dup_date(group)
	if dupes == True: total += 1

print(total/trials)
