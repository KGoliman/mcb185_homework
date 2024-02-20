import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])
total = 0

def calendars(days):
	calendar = []
	for i in range(days):
		calendar.append(0)
	return calendar

def birthdays(days, people):
	calendar = calendars(days)
	bday = []
	for i in range(people):
		bd = random.randint(0, days -1)
		bday.append(bd)
	bday.sort()
	for date in bday:
		calendar[date] += 1
	return calendar
		
def bday_dupe(days, people):
	bdays = birthdays(days, people)
	for date in bdays:
		if date > 1:
			return True
			break

for i in range(trials):
	bdays = bday_dupe(days, people)
	if bdays == True:
		total += 1

print(total/trials)