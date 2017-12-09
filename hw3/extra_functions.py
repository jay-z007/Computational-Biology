# def DFS(v, graph, visited, path=[]):
#     visited[v] = True
#     # print v
#     path.append(v)
#     if v not in graph:
#         return

#     for i in graph[v]:
#         if not visited[i]:
#             DFS(i, graph, visited, path)
#     return


# def _fleury(g, curr):
#     # print "\n", curr, g
#     if curr not in g:
#         trail.append(curr)
#         return

#     if len(g[curr]) == 1:
#         dst = g[curr][0]
#         g[curr].remove(dst)
#         if len(g[curr]) == 0:
#             g.pop(curr, None)

#         trail.append(curr)
#         _fleury(g, dst)
#         return

#     for dst in g[curr]:
#         if not is_bridge(g, dst):
#             g[curr].remove(dst)
#             if len(g[curr]) == 0:
#                 g.pop(curr, None)
#             trail.append(curr)
#             _fleury(g, dst)
#             return



# def is_bridge(g, u, v, start):
#     g[u].remove(v)
#     # g[u].remove(current_vertex)
#     bridge = not is_connected(g, start)
#     if bridge:
#         return True
#     else:
#         return False


# def is_connected(G, start):
#     visited = {key: False for key in V}

#     count = DFSCount(start, G, visited)
#     print count

#     return False if count != len(V) else True



# def DFSCount(v, graph, visited):
#     count = 1
#     visited[v] = True

#     if v not in graph:
#         return 1

#     for i in graph[v]:
#         if not visited[i]:
#             count = count + DFSCount(i, graph, visited)
#     return count
