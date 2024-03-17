import dogma
import sys
import math
import mcb185

file = sys.argv[1]
w = int(sys.argv[2])
e = float(sys.argv[3])

def entropy(probs):
	h = 0
	for p in probs:
		h -= p * math.log2(p)
	return h

def dust(seq, w, e):
	copy_list = list(seq)
	for i in range(len(seq) - w + 1):
		s = seq[i:i+w]
		ent = []
		a_count = s.count('A')
		c_count = s.count('C')
		g_count = s.count('G')
		t_count = s.count('T')
		if a_count !=0:
			a = a_count/w
			ent.append(a)
		if c_count !=0:
			c = c_count/w
			ent.append(c)
		if g_count !=0:
			g = g_count/w
			ent.append(g)
		if t_count !=0:
			t = t_count/w
			ent.append(t)
		se = entropy(ent)
		if se < e:
			for k in range(len(s)):
				copy_list[i+k] = 'N'
	copy_list = ''.join(copy_list)
	return copy_list

for defline, seq in mcb185.read_fasta(file):
	dust_seq = dust(seq[:180], w, e)
	print(f'>{defline}')
	print(dust_seq)