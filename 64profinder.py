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

'''
for frame in range(3):
	for protein in pro_finder(test_seq[frame:], 2):
		print(protein)

for frame in range(3):
	print(frame, test_seq[frame:])
	for i in range(0, len(test_seq) - 3 + 1, 3):
		print(test_seq[i:i+3])
		
seq = 'ATGCGGCTAGCTGCAGGATCTTAGTCTCCGATAC'
# when got to *(stop), = new orf, put old to list and make new list
'''