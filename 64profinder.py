import dogma
import sys
import mcb185


file = sys.argv[1]
#min = int(sys.argv[2])

test_seq = "TCGAGGATCGATTACGGCAGCTTACTTAGGCGGATTAGGCTAGGCTGATGGCTAGC"

def pro_finder(defline, test_seq, min): # use this function again for rev_seq and for [1] and [2]
	proteins = []
	for orf in dogma.translate(test_seq).split("*"):
		if 'M' in orf:
			start = orf.find('M')
			protein = orf[start:]
			if len(protein) >= min:
				proteins.append(protein)
	for i in range(len(proteins)):
		print(f'>{defline.split(" ")[0]}-prot-{i}')
		print(proteins[i])

for defline, seq in mcb185.read_fasta(file):
	frame = dogma.sixframe(seq)
	pro_finder(defline, frame, 100)