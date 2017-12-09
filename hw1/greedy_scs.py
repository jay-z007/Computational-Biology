import itertools as it

class fasta(object):
	"""docstring for fasta"""

	def __init__(self, fasta_id, value):
		super(fasta, self).__init__()
		self.fasta_id = fasta_id
		self.value = value


def fasta_read(filename):
	read_data = []

	with open(filename, 'r') as file:
		data = file.read()
	
	data = data.split('>')[1:]

	for line in data:
		words = line.split()
		fasta_id = words[0]
		value = ''.join(words[1:])
		# print value
		read_data.append(fasta(fasta_id, value))
		# read_data.append(value)

	return read_data

def find_overlap(s1, s2):
	max1 = 0
	ans = ""

	for i in range(1, min(len(s1), len(s2))):
		if s2[0:i] == s1[-i:]:
			if max1 < i:
				max1 = i
				ans = s1+s2[i:]

	return max1

def get_max_overlap(reads):
	read_a, read_b = None, None
	best_olen = 0
	for a, b in it.permutations(reads, 2):
		o_len = find_overlap(a, b)
		if o_len > best_olen:
			best_olen = o_len
			read_a, read_b = a, b

	return read_a, read_b, best_olen


def greedy_scs(reads):
	read_a, read_b, o_len = get_max_overlap(reads)
	while o_len > 0:
		reads.remove(read_a)
		reads.remove(read_b)
		reads.append(read_a+read_b[o_len: ])
		read_a, read_b, o_len = get_max_overlap(reads)

	return ''.join(reads)

reads = []

data = fasta_read("./data/rosalind_long.txt")
for i in data:
	reads.append(i.value)

ans = greedy_scs(reads)

print ans, len(ans)
