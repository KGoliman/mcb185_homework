import dogma
import sys
import mcb185


file = sys.argv[1]

def signal_peptide(seq):
	first30 = seq[0:30]
	for i in range(len(first30) - 8 + 1):
		tot_kd = 0
		seq = first30[i:i+8]
		for aa in seq:
			tot_kd += dogma.kdhydrophobicity(aa)
		avg_kd = tot_kd / 8
		if avg_kd >= 2.5 and 'P' not in seq:
			return True
		else: continue
	return False

def transmembrane(seq):
	after30 = seq[30:]
	for i in range(len(after30) - 11 + 1):
		tot_kd = 0
		seq = after30[i:i+11]
		for aa in seq:
			tot_kd += dogma.kdhydrophobicity(aa)
		avg_kd = tot_kd / 11
		if avg_kd >= 2.0 and 'P' not in seq:
			return True
		else: continue
	return False

for defline, prot in mcb185.read_fasta(file):
		if signal_peptide(prot) == True and transmembrane(prot) == True:
			print(f'>{defline[:60]}')