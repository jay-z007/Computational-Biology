kmers = ""

def find_next(super_string,overlap_len):
	global kmers
	i = 0

	if not kmers:
		return super_string

	if len(kmers) == 1:
		start = kmers[i][0]
		kmers.pop(i)
		return start + super_string 

	i = 0
	while i < len(kmers):
		if super_string[-overlap_len:] == kmers[i][:overlap_len]:
			end = kmers[i][-1]
			kmers.pop(i)
			return super_string + end
		i+=1
	return super_string


def main():
	global kmers	

	file_name = './data/rosalind_pcov.txt'
	with open(file_name) as f:
		kmers = f.read().strip()

	kmers = kmers.split('\n')
	super_string = kmers.pop(0)

	overlap_len = len(kmers[0])-1

	while kmers:
		super_string = find_next(super_string,overlap_len)

	i = len(super_string)//2
	while i < len(super_string):
		if super_string[i:] == super_string[:len(super_string)-i]:
			super_string = super_string[:i]
			break
		i += 1
	
	print super_string

if __name__ == '__main__':
	main()