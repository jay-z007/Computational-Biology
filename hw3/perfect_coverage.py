inp = """ATTAC
TACAG
GATTA
ACAGA
CAGAT
TTACA
AGATT"""

def find_next(super_string,overlap_len):
	global inp
	i = 0

	# if super_string == "AAAATTCTCAAACATGAGGTTTATAACTGACTATCAGGTACGCGCGACTCTGGCATATGATGATCGG":
	# 	pass
	if not inp:
		return super_string

	if len(inp) == 1:
		start = inp[i][0]
		inp.pop(i)
		return start + super_string 
	i = 0
	while i < len(inp):
		if super_string[-overlap_len:] == inp[i][:overlap_len]:
			end = inp[i][-1]
			inp.pop(i)
			return super_string + end
		i+=1
	return super_string



# import pdb; pdb.set_trace()
def main():
	global inp	

	file_name = 'rosalind_pcov.txt'
	with open(file_name) as f:
		inp = f.read().strip()

	inp = inp.split('\n')
	super_string = inp.pop(0)

	overlap_len = len(inp[0])-1

	while inp:
		# print inp,"\n\n"
		# print len(inp)
		super_string = find_next(super_string,overlap_len)
		# print super_string

	i = len(super_string)//2
	while i < len(super_string):
		if super_string[i:] == super_string[:len(super_string)-i]:
			super_string = super_string[:i]
			break
		i += 1
	
	print super_string

if __name__ == '__main__':
	main()