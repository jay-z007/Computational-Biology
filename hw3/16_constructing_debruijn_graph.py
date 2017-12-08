import sys

def reverse_compliment(kmer):
    reverse = {'A':'T', 'G':'C', 'T':'A', 'C':'G'}
    kmer_rc = ""

    for k in kmer: kmer_rc+=reverse[k]
    return kmer_rc[::-1]


def main():
    with open('data/rosalind_dbru.txt', 'rt') as in_file:
        kmers = in_file.read()

    graph = {}

    kmers = kmers.split()
    kmers.extend(map(reverse_compliment, kmers))
    # print len(set(kmers)), len(kmers)
    kmers = set(kmers)

    for kmer in kmers:
        l_kmer, r_kmer = kmer[:-1], kmer[1:]
        # print kmer, l_kmer, r_kmer
        graph.setdefault(l_kmer, []).append(r_kmer)
        # graph.append((l_kmer, r_kmer))

    for k in sorted(graph):
        for i in graph[k]:
            print "("+k+", "+i+")"



if __name__ == '__main__':
    main()