import random
import math

in_circle = 0
out_circle = 0
while True:
	x = random.random()
	y = random.random()
	distance_origin = math.sqrt(x**2 + y**2)
	if distance_origin < 1: in_circle += 1
	else:					out_circle += 1
	montecarlo_pi = (4 * in_circle) / (in_circle + out_circle)
	print(montecarlo_pi)