def transcribe(dna):
	return dna.replace('T', 'U')


def revcomp(dna):
	rc = []
	for nt in dna[::-1]:
		if   nt == 'A': rc.append('T')
		elif nt == 'C': rc.append('G')
		elif nt == 'G': rc.append('C')
		elif nt == 'T': rc.append('A')
		else:           rc.append('N')
	return ''.join(rc)

def sixframe(seq):
	frame = []
	rev_comp = revcomp(seq)
	for i in range(3):	
		frame.append(seq[i:])
		frame.append(rev_comp[i:])
	return ''.join(frame)

def translate(dna):
	aas = []
	for i in range(0, len(dna), 3):
		codon = dna[i:i+3]
		if codon == 'ATG': aas.append('M')
		elif codon == 'TAA' or codon == 'TAG' or codon == 'TGA': aas.append('*')
		elif codon == 'ATT' or codon == 'ATC' or codon == 'ATA': aas. append('I')
		elif codon == 'ACT' or codon == 'ACG' or codon == 'ACC' or codon == 'ACA': aas. append('T')
		elif codon == 'AAT' or codon == 'AAC': aas. append('N')
		elif codon == 'AAA' or codon == 'AAG': aas. append('K')
		elif codon == 'AGT' or codon == 'AGC' or codon == 'TCA' or codon == 'TCG' or codon == 'TCC' or codon == 'TCT': aas. append('S')
		elif codon == 'AGA' or codon == 'AGC' or codon == 'CGT' or codon == 'CGA' or codon == 'CGT' or codon == 'CGC': aas. append('R')
		elif codon == 'GTA' or codon == 'GTC' or codon == 'GTG' or codon == 'GTT': aas. append('V')
		elif codon == 'GCA' or codon == 'GCC' or codon == 'GCT' or codon == 'GCG': aas. append('A')
		elif codon == 'GAT' or codon == 'GAC': aas. append('D')
		elif codon == 'GAG' or codon == 'GAA': aas. append('E')
		elif codon == 'GGA' or codon == 'GGT' or codon == 'GGC' or codon == 'GGG': aas. append('G')
		elif codon == 'TTT' or codon == 'TTC': aas. append('F')
		elif codon == 'TTA' or codon == 'TTG' or codon == 'CTA' or codon == 'CTT' or codon == 'CTC' or codon == 'CTG': aas. append('L')
		elif codon == 'TCA' or codon == 'TCT' or codon == 'TCG' or codon == 'TCC': aas. append('S')
		elif codon == 'TAT' or codon == 'TAC': aas. append('Y')
		elif codon == 'TGT' or codon == 'TGC': aas. append('C')
		elif codon == 'TGG': aas. append('W')
		elif codon == 'CCC' or codon == 'CCA' or codon == 'CCG' or codon == 'CCT': aas. append('P')
		elif codon == 'CAC' or codon == 'CAT': aas. append('H')
		elif codon == 'CAA' or codon == 'CAG': aas. append('Q')
		else: aas.append('X')
	return ''.join(aas)

def gc_comp(seq):
    return (seq.count('C') + seq.count('G')) / len(seq)

def gc_skew(seq):
	c = seq.count('C')
	g = seq.count('G')
	if c + g == 0: return 0
	return (g-c)/(g+c)
'''
def pro_finder(seq, min)
	proteins = []
	for orf in dogma.translate(seq).split("*")
		if 'M' in orf:
			start = orf.find('M')
			end = orf.find('*')
			proteins = orf[start:end:]
			if len(proteins) >= min:
				proteins.append(orf)
	return proteins
'''

def kdhydrophobicity(b):
	kds = 0
	if   b == 'A' or b == 'a': kds +=   1.8
	elif b == 'C' or b == 'c': kds +=   2.5
	elif b == 'D' or b == 'd': kds +=  -3.5
	elif b == 'E' or b == 'e': kds +=  -3.5
	elif b == 'F' or b == 'f': kds +=   2.8
	elif b == 'G' or b == 'g': kds +=  -0.4
	elif b == 'H' or b == 'h': kds +=  -3.2
	elif b == 'I' or b == 'i': kds +=   4.5
	elif b == 'K' or b == 'k': kds +=  -3.9
	elif b == 'L' or b == 'L': kds +=   3.8
	elif b == 'M' or b == 'm': kds +=   1.9
	elif b == 'N' or b == 'n': kds +=  -3.5
	elif b == 'P' or b == 'p': kds +=  -1.6
	elif b == 'Q' or b == 'q': kds +=  -3.5
	elif b == 'R' or b == 'r': kds +=  -4.5
	elif b == 'S' or b == 's': kds +=  -0.8
	elif b == 'T' or b == 't': kds +=  -0.7
	elif b == 'V' or b == 'v': kds +=   4.2
	elif b == 'W' or b == 'w': kds +=  -0.9
	elif b == 'Y' or b == 'y': kds +=  -1.3
	else: kds += 0
	return kds