import sys
import math

probs = []
for arg in sys.argv[1:]:
	f = float(arg)
	assert(f > 0 and f < 1)
	probs.append(float(arg))

total = 0
for p in probs: total += p
if not math.isclose(total, 1.0):
	sys.exit('error: total must sum to one')

h = 0
for p in probs:
	h -= p * math.log2(p)

print(p)