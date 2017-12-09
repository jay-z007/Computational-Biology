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


class Overlap_graphs(object):
    """docstring for Overlap_graphs"""

    def find_overlap(self, s1, s2, overlap):
        if s2[:overlap] == s1[-1 * overlap:]:
            return True
        return False

    def make_adj_list(self, vertices, overlap):
        orders = []

        for i in range(len(vertices)):
            for j in range(i + 1, len(vertices)):
                if self.find_overlap(vertices[i][1], vertices[j][1], overlap):
                    orders.append([vertices[i][0], vertices[j][0]])

                if self.find_overlap(vertices[j][1], vertices[i][1], overlap):
                    orders.append([vertices[j][0], vertices[i][0]])

        return orders


def main():
    filename = "./data/rosalind_grph.txt"
    data = fasta_read(filename)
    vertices = {}

    for i in data:
        vertices[i.fasta_id] = i.value
    overlap = 3

    obj = Overlap_graphs()
    list_vertices = [[k, v] for k, v in vertices.items()]
    ans = obj.make_adj_list(list_vertices, overlap)

    for item in ans:
        print item[0], item[1]


if __name__ == '__main__':
    main()
