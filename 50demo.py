amount = 0
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
	
def standev():
	mean = mean(vals)
	total = 0
	for val in vals:
		value = (val[1:] - mean) ** 2
		total += value
	return math.sqrt(total / final)

def median():
	if len(val) % 2 == 0: med = val[len(val) // 2] # odd - numbered list
	else: med = ((val[len(val/2)] + val[len((val/2)+1)])) / 2
	print(med)

print(minmax())
print(mean())
print(standev())
print(median())