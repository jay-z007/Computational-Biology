
class fasta(object):
	"""docstring for fasta"""

	def __init__(self, fasta_id, value):
		super(fasta, self).__init__()
		self.fasta_id = fasta_id
		self.value = value
		

# inplement properly
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

def kmp(P,T):
	n = len(T)
	m = len(P)
	matches = []
	pi = partialMatchTable(P)
	q = 0
	i = 0
	while i < n:
		if P[q] == T[i]:
			q += 1
			i += 1
			if q == m:
				matches.append(i-q)
				q = pi[q-1]
			else:
				if q == 0:
					i += 1
				else:
					q = pi[q-1]
					return matches