import os

from collections import defaultdict

alphabet = [
    'A',
    'C',
    'G',
    'T',
]

def dist(a, b):

    if a == b:
        return 0
    else:
        return 1

def seq_dist(a, b):

    summ = 0

    for i in range(len(a)):
        if a[i] != b[i]:
            summ += 1

    return summ

class Node(object):
    def __init__(self, index, leaf):

        self.index = index
        self.leaf = leaf
        self.children = []
        self.edges = []
        self.text = ''
        self.score = defaultdict(int)
        self.scored = False

    def reinit(self):

        self.score = defaultdict(int)
        self.scored = False
        return None

    def is_ripe(self):

        if self.leaf:
            return True

        else:
            for item in self.children:
                if not nodelist[item].scored:
                    return False
        return True

    def add_node(self, c_index):

        self.children.append(c_index)
        self.edges.append(0)
        return None

    def scoring(self, curr_letter):

        if self.leaf:
            for letter in alphabet:
                if letter == self.text[curr_letter]:
                    self.score[letter] = 0
                else:
                    self.score[letter] = float('inf')
        else:
            for letter in alphabet:
                for item in self.children:
                    self.score[letter] += min([
                        nodelist[item].score[i] + dist(letter, i)
                        for i in alphabet
                    ])

        self.scored = True
        return None

def interpreter(conn):

    nn = int(conn.readline().strip())
    nl = [Node(i, True) for i in range(nn)]

    for j, raw_line in enumerate(conn):
        line = raw_line.strip().split('->')
        node_val = int(line[0])

        if node_val == len(nl):
            nl.append(Node(node_val, False))

        if node_val > len(nl):
            print("Unexpected node")

        if j < nn:
            nl[node_val].add_node(j)
            nl[j].text = line[1]

        if j >= nn:
            nl[node_val].add_node(int(line[1]))

    return nl

def tree_scoring(curr_letter):

    for node in nodelist:
        if node.leaf:
            node.scoring(curr_letter)

    while not nodelist[-1].scored:
        for node in nodelist:
            if not node.scored:
                if node.is_ripe():
                    node.scoring(curr_letter)
    return None

def tree_pruning(node, parent_letter=''):

    if node.leaf:
        return None

    mini = float('inf')
    choice = ''

    for letter in alphabet:
        s = node.score[letter]

        if parent_letter != letter:
            s += 1

        if s < mini:
            mini = s
            choice = letter

    node.text += choice
    for i in node.children:
        tree_pruning(nodelist[i], choice)

    return None

def tree_edge_weighter(node):

    global running_sum

    if node.leaf:
        return None

    for index, item in enumerate(node.children):
        dd = seq_dist(node.text, nodelist[item].text)
        running_sum += dd
        node.edges[index] = dd
        tree_edge_weighter(nodelist[item])
    return None

def tree_printer(node, conn):

    if node.leaf:
        return None

    for index, item in enumerate(node.children):
        child = nodelist[item]
        conn.write(node.text + '->' + child.text + ':' +
                   str(node.edges[index]) + '\n')
        conn.write(child.text + '->' + node.text + ':' +
                   str(node.edges[index]) + '\n')
        tree_printer(child, conn)
    return None

if __name__ == '__main__':

    with open('rosa.txt', 'r') as f:
        nodelist = interpreter(f)

    seq_len = len(nodelist[0].text)

    for i in range(seq_len):
        tree_scoring(i)
        tree_pruning(nodelist[-1])

        for node in nodelist:
            node.reinit()

    running_sum = 0
    tree_edge_weighter(nodelist[-1])

    with open('parsimony_out.txt', 'w') as out:
        out.write(str(running_sum) + '\n')
        tree_printer(nodelist[-1], out)

"""
import sys
import numpy as np

# input_file = "rosa.txt"

# with open(input_file, 'rt') as f:
#     data = f.read()

# data = data.split('\n')
# n = int(data[0])
# data = data[1:]
# v = []
# labels = []
# for i in range(n):
#     line = data[i].split('->')
#     v.append((int(line[0]), i))
#     labels.append(line[1])

# data = data[n:]
# while data:
#     line = data.pop(0).split('->')
#     v.append((int(line[0]), int(line[1])))

# # print v, labels

# # m, total node count
# m = 2 * n - 1
# # print character
# # compute tree and reverse-tree from edges
# tree = {}
# parent = {}
# tag = {}
# alphabet = sorted(['A', 'C', 'G', 'T'])
# # print alphabet
# len_a = len(alphabet)
# char_len = len(labels)
# d = dict(zip(alphabet, range(len_a)))
# sk = np.ndarray(shape=(m, len_a), dtype=int)
# s = [''] * m

# # print d


# def dfs(node):
#     if node < n:
#         return
#     r = tree[node][1]
#     l = tree[node][0]
#     dfs(l)
#     dfs(r)

#     for k in range(len_a):
#         transition = np.ones(len(alphabet))
#         transition[k] = 0
#         sk[node, k] = min(sk[l] + transition) + min(sk[r] + transition)

#     return


# def dfs_s(node):
#     if node < n:
#         # leaf is at tree botton, simply return
#         return

#     c = sk[node, :]
#     if node == root:
#         # when root simply choose the min score ever
#         s[node] = alphabet[c.argmin()]
#     else:
#         pnode = parent[node]
#         j = d[s[pnode]]
#         mask = np.ones(len(alphabet), dtype=int)
#         mask[j] = 0
#         c += mask
#         s[node] = alphabet[c.argmin()]

#     lnode = tree[node][0]
#     rnode = tree[node][1]
#     dfs_s(lnode)
#     dfs_s(rnode)

# for i, edge in enumerate(v):
#     node = edge[0]
#     child = edge[1]
#     tag[node] = 0
#     sk[node] = [0] * len_a
#     tree.setdefault(node, []).append(child)
#     parent[child] = node

# root = parent[tree.keys()[0]]
# while root in parent.keys():
#     root = parent[root]


# def smallParsimony(n, edges, character):

#     for i, edge in enumerate(edges):
#         if i < n:
#             tag[child] = 1
#             # sk[child] = {}
#             for j, symbol in enumerate(alphabet):
#                 if character[i] == symbol:
#                     sk[child][j] = 0
#                     s[child] = symbol
#                 else:
#                     sk[child][j] = sys.maxint

#     dfs(root)

#     dfs_s(root)
#     parsimony = sk[root].min(axis=0)

#     return parsimony, s, 1, 1


# def main():
# for line in input_file:
# n = 4
# v = [(4, 0), (4, 1), (5, 2), (5, 3), (6, 4), (6, 5)]
# labels = ['CAAATCCC', 'ATTGCGAC', 'CTGCGCTG', 'ATGGACGA']
# parsimony = 0

# for i in range(len(labels[0])):
#     label = [row[i] for row in labels]
#     (p, e, r, l) = smallParsimony(n, v, label)
#     parsimony += p

# print parsimony

# if __name__ == '__main__':
#     main()
"""
