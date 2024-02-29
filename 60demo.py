import mcb185
import sys

k = 3
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	print(defline[:30], seq[:40], len(seq))
	defwords = defline.split()
	name = defwords[0]
	nts = 'ATCGN'
	for nt in nts:
		print(seq.count(nt) / len(seq), end='\t')
	print()
'''
	words = defline.split()
	print(words[0], len(seq))

	pro = []
	for i in range(len(seq) - k + 1, 3):
		codon = seq[i:i+3]
		print(codon)
#		aa = translate(codon) if we have function to translate
		pro.append(aa)
'''