import sys
colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])
assert(0 <= R <= 255)
assert(0 <= G <= 255)
assert(0 <= B <= 255)
target = []
target.append(R)
target.append(G)
target.append(B)

def dtc(P, Q):
    d = 0
    for p, q in zip(P, Q):
        d += abs(p - q)
    return d

def minimum(vals):
	mini = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val
	return mini

with open(colorfile) as fp:
	results = []
	for line in fp:
		words = line.split()
		number = words[2].split(',')
		for i in range(0, len(number)):
			number[i] = int(number[i])
		for i in range(len(number)):
			result = dtc(target, number)
			results.append(result)
	fin_res = results[0:len(results):3]
	min_fin_res = minimum(fin_res)
	print(fin_res)
	print(min_fin_res)