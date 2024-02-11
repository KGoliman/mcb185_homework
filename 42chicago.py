import random

zerogames = 0
totalscore = 0
gameplayed = 1000
for i in range(gameplayed):
	score = 0
	for roundnumber in range(2, 13):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		if d1 + d2 == roundnumber:
			score += roundnumber
	totalscore += score
	if score == 0:
		zerogames += 1

print(zerogames/gameplayed)
print(totalscore/gameplayed)
print(zerogames)