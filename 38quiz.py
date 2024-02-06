# co-author: Jonathan Raigosa

sign_flip = 1
start = 4
for i in range(10):
	gl_denom = (1 + (2 * i))
	gl = 4 / gl_denom
	sign_flip = -sign_flip
	start = start + (sign_flip * gl)
	print(gl)

for i in range(10):
	gl = -((-1) ** i) * (4 / (1 + (2 * i)))
	gl = 4 - gl
	print(gl)

	