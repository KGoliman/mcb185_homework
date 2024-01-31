import sys

def kdhydrophobicity(b):
	if   b == 'A' or b == 'a': return  1.8
	elif b == 'C' or b == 'c': return  2.5
	elif b == 'D' or b == 'd': return -3.5
	elif b == 'E' or b == 'e': return -3.5
	elif b == 'F' or b == 'f': return  2.8
	elif b == 'G' or b == 'g': return -0.4
	elif b == 'H' or b == 'h': return -3.2
	elif b == 'I' or b == 'i': return  4.5
	elif b == 'K' or b == 'k': return -3.9
	elif b == 'L' or b == 'L': return  3.8
	elif b == 'M' or b == 'm': return  1.9
	elif b == 'N' or b == 'n': return -3.5
	elif b == 'P' or b == 'p': return -1.6
	elif b == 'Q' or b == 'q': return -3.5
	elif b == 'R' or b == 'r': return -4.5
	elif b == 'S' or b == 's': return -0.8
	elif b == 'T' or b == 't': return -0.7
	elif b == 'V' or b == 'v': return  4.2
	elif b == 'W' or b == 'w': return -0.9
	elif b == 'Y' or b == 'y': return -1.3
	else: sys.exit('error: amino acid not recognized')	

print(kdhydrophobicity('C'))
print(kdhydrophobicity('c'))
print(kdhydrophobicity('p'))
print(kdhydrophobicity('x')) # not an amino acid