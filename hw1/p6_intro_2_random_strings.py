import math


class Random_string(object):
    """docstring for Random_string"""

    def find_prob(self, s, A):
        s = [0 if i is 'G' or i is 'C' else 1 for i in s]
        B = []

        for i in range(len(A)):
            res = 0
            gc = []
            gc.append(A[i] / 2)
            gc.append((1 - A[i]) / 2)

            for char in s:
                res += math.log(gc[char], 10)

            B.append(res)

        return B


def main():
    r = Random_string()

    s = "TCCTCTCGGCAAGCGTTTCGAACAGTCGCTATGCATTAACACGCTTCCCTGTTAACCAAGCGTAGGCCAGATAGGCCGGCCATAATACCTCCTTAAT"
    # A = [0.129, 0.287, 0.423, 0.476, 0.641, 0.742, 0.783]
    A = [
        0.091, 0.116, 0.205, 0.276, 0.279, 0.357, 0.444, 0.454, 0.538, 0.570,
        0.615, 0.673, 0.772, 0.824, 0.883, 0.916
    ]

    res = r.find_prob(s, A)
    for i in res:
        print "{0:.3f}".format(i),


if __name__ == '__main__':
    main()
