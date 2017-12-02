import sys

def smallParsimony(n, edges, character):
    # m, total node count
    m = 2*n-1    
    print character    
    # compute tree and reverse-tree from edges
    tree = {}
    parent = {}
    tag = {}
    alphabet = ['A', 'C', 'G', 'T']
    sk = {}

    def dfs(root):
        stack = []
        stack.append(root)
        

    for i, edge in enumerate(edges):
        node = edge[0]
        child = edge[1]
        tag[node] = 0
        sk[node] = {}
        if i < n:
            tag[child] = 1
            sk[child] = {}
            for symbol in alphabet:
                if character[i] == symbol:
                    sk[child][symbol] = 0
                else:
                    sk[child][symbol] = sys.maxint

        tree.setdefault(node,[]).append(child)
        parent[child] = node

    root = parent[tree.keys()[0]]
    while root in parent.keys():
        root = parent[root]

    dfs(root)

    # print sk
    print "\n\n"
    # print tree
    # print parent

    return 1,1,1,1


def main():
    n = 4
    v = [(4,0),(4,1),(5,2),(5,3),(6,4),(6,5)]
    labels = ['CAAATCCC', 'ATTGCGAC', 'CTGCGCTG', 'ATGGACGA']
    for i in range(len(labels[0])):
        label = [row[i] for row in labels]
        (p,e,r,l) = smallParsimony(n,v,label)
    # assert p == 16

if __name__ == '__main__':
    main()