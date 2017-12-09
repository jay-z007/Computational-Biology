from utilities import fasta_read


class genome_assembly(object):

    def find_overlap(self, s1, s2):
        max1 = 0
        ans = ""

        for i in range(1, min(len(s1), len(s2))):
            if s2[0:i] == s1[-i:]:
                if max1 < i:
                    max1 = i
                    ans = s1 + s2[i:]

        s1, s2 = s2, s1

        for i in range(1, min(len(s1), len(s2))):
            if s2[0:i] == s1[-i:]:
                if max1 < i:
                    max1 = i
                    ans = s1 + s2[i:]

        return ans, max1

    def scs_greedy(self, reads):

        size = len(reads)
        print "size = ", size

        while size != 1:
            res = ""
            max1 = 0
            l, r = 0, 0

            for i in range(size):
                for j in range(i + 1, size):

                    overlap, o_len = self.find_overlap(reads[i], reads[j])

                    if max1 < o_len:
                        res = overlap
                        max1 = o_len
                        l = i
                        r = j

            size -= 1

            if max1 == 0:
                reads[0] += reads.pop(size)
            else:
                reads.pop(r)
                reads[l] = res

        return reads


def main():
    obj = genome_assembly()

    reads = []
    data = fasta_read("./data/rosalind_long.txt")
    for i in data:
        reads.append(i.value)

    print sum([len(i) for i in reads])

    ans = obj.scs_greedy(reads)

    print len(ans[0])


if __name__ == '__main__':
    main()
