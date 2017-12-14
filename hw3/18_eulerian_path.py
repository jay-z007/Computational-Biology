from copy import copy, deepcopy
import pdb
import sys
sys.setrecursionlimit(2100)
pdb.set_trace()

trail = []
V = []


def DFS(v, graph, visited, path=[]):
    visited[v] = True
    # print v
    path.append(v)
    if v not in graph:
        return

    for i in graph[v]:
        if not visited[i]:
            DFS(i, graph, visited, path)
    return


# def DFS(v, graph, visited, path=[]):
#     # print v
#     path.append(v)
#     nodes_to_visit = graph[v][::-1]
#     visited[v] = True

#     while nodes_to_visit:

#         v = nodes_to_visit.pop()
#         # print v
#         # unsure of this
#         if v not in graph:
#             continue
#         visited[v] = True

#         if

#         children = []
#         for i in graph[v]:
#             if not visited[i]:
#                 children.append(i)

#         nodes_to_visit.extend(children[::-1])
#         print nodes_to_visit

#     return


def edges(G):
    edge_list = []
    for k in sorted(G):
        for i in G[k]:
            edge_list.append((k, i))

    return edge_list


def vertices(G):
    counts = {key: 0 for key in G.keys()}

    for node in G:
        for dst in G[node]:
            if dst not in counts:
                counts[dst] = 0

    return counts.keys()


def semi_balanced_nodes(G):
    counts = {key: 0 for key in G.keys()}

    for node in G:
        counts[node] -= len(G[node])

        for dst in G[node]:
            if dst in counts:
                counts[dst] += 1
            else:
                counts[dst] = 1

    un_balanced_nodes = [(k, v) for k, v in counts.items() if v != 0]
    return un_balanced_nodes


def is_bridge(g, v):
    ver = vertices(g)
    visited = {key: False for key in ver}
    path = []
    DFS(v, g, visited, path)
    # print path
    # print len(path), len(V)
    return len(path) != len(ver)



def _fleury(g, curr):
    # print "\n", curr, g
    count = 0
    while curr in g:
        # count+=1
        # print count
        if len(g[curr]) == 1:
            dst = g[curr][0]
            g[curr].remove(dst)
            if len(g[curr]) == 0:
                g.pop(curr, None)
            trail.append(curr)
            curr = dst
            # _fleury(g, dst)
            continue

        for dst in g[curr]:
            if not is_bridge(g, dst):
                g[curr].remove(dst)
                if len(g[curr]) == 0:
                    g.pop(curr, None)
                trail.append(curr)
                curr = dst
                break
                # _fleury(g, dst)
                # return
        if all([is_bridge(g,dst) for dst in g[curr]]):
            return

    if curr not in g:
        trail.append(curr)
        return


def fleury(G):
    '''
		checks if G has eulerian cycle or trail
	'''
    odn = semi_balanced_nodes(G)
    # print odn
    st = min(odn,key=lambda o: o[1])
    g = copy(G)
    _fleury(deepcopy(g), st[0])
    print trail
    # if len(odn) > 2 or len(odn) == 1:
    #     return 'Not Eulerian Graph'
    # else:
        # g = copy(G)
    #     if len(odn) == 2:

    #         i = 0
    #         while len(set(trail)) != len(V):
    #             if odn[i][0] in G:
    #                 print "ohh yeah", odn[i]
    #                 _fleury(deepcopy(g), odn[i][0])
    #             print trail, V
    #             i += 1

    #     else:
    #         u = list(g)[0]
    #         _fleury(deepcopy(g), u)

    # print g

def main():
    global V

    data = """0 -> 2
1 -> 3
2 -> 1
3 -> 0,4
6 -> 3,7
7 -> 8
8 -> 9
9 -> 6"""
    with open('../../compBio/hw3/eulerian_path.txt', 'rt') as in_file:
        data = in_file.read()

    graph = {}

    data = data.split('\n')
    data = [i.split('->') for i in data]
    for d in data:
        s, d = d
        s, d = s.strip(), d.strip().split(',')
        graph.setdefault(s, []).extend(d)

    # print graph
    V = vertices(graph)
    fleury(graph)

    # print is_bridge(graph, '7')
    # DFS('6', graph, visited)
    # print trail
    # odn = semi_balanced_nodes(graph)
    # print edges(graph)
    # print odn
    # print V
    # graph['6'].remove('3')
    # print is_connected(graph, V, odn)

if __name__ == '__main__':
    main()