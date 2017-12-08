def correct_incorrect(counts, orig_seqs):

    correct = []
    incorrect = []

    for s in counts:

        if counts[s] >= 2:
            correct.append(s)

        elif s in orig_seqs:
            incorrect.append(s)

    return correct, incorrect

def hamming(seq1, seq2):

    mutations = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            mutations += 1

    return mutations

def corrections(correct, incorrect):

    corrected = []
    for seq1 in incorrect:
        for seq2 in correct:
            if hamming(seq1, seq2) == 1:
                corrected.append([seq1, seq2])

    return corrected

if __name__ == "__main__":

    from Bio import SeqIO
    from Bio import Seq

    seqs = []
    orig_seqs = []
    counts = {}

    with open("rosalind_corr.txt", 'r') as f:

        for s in SeqIO.parse(f, "fasta"):
            seq = str(s.seq)
            orig_seqs.append(seq)
            seqs.append(seq)
            seqs.append(str(s.seq.reverse_complement()))
    
    for seq in seqs:
        if seq in counts:
            counts[seq] += 1
        else:
            counts[seq] = 1

    correct, incorrect = correct_incorrect(counts, orig_seqs)
    corrs = corrections(correct, incorrect)

    # with open("CORR.txt", 'w') as o:
    for i in corrs:
        print "->".join(i)
