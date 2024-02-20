import sys
colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])
assert(0 <= R <= 255)
assert(0 <= G <= 255)
assert(0 <= B <= 255)
target = (R, G, B)

def dtc(P, Q):
    d = 0
    for p, q in zip(P, Q):
        d += abs(p - q)
    return d

min_d = 256 * 3
color = None

with open(colorfile) as fp:
	results = []
	line = []
	for line in fp:
		words = line.split()
		r, g, b = words[2].split(',')
		r = int(r)
		g = int(g)
		b = int(b)
		d = dtc((r, g, b), target)
		if d < min_d:
			min_d = d
			color = words[0]

print(color)