amount = 0
vals = [4, 5, 6, 3, 5, 4]

for val in vals:
	amount += 1
	final = amount

def minmax(vals):
	mini = vals[0]
	maxi = vals[0]
	for val in vals:
		if val < mini: mini = val
		if val > maxi: maxi = val
	return mini, maxi

def mean(vals):
	total = 0
	for val in vals: total += 1
	return total / len(vals)
	
def standev(vals):
	total = 0
	stdvmn = mean(vals)
	for val in vals: total += ((val - stdvmn) ** 2)
	return round(((total / len(vals))**0.5), ndigits = 0)

def median(vals):
	vals.sort()
	midx1 = vals[len(vals) // 2]
	midx2 = vals[(len(vals) // 2) - 1]
	if len(vals) % 2 == 1: med = midx1
	else: med = (midx1 + midx2) / 2
	return med

print(minmax(vals))
print(mean(vals))
print(standev(vals))
print(median(vals))