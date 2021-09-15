def dfs(graph, node, visited, stack, path):
    if node in path:
        return True
    path.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs(graph, neighbor, visited, stack, path):
                return True
    visited.add(node)
    stack.append(node)
    return False


def topological_order(edges, n):
    graph = dict()

    for i in range(1, n+1):
        graph[i] = set()

    for edge in edges:
        graph[edge[0]].add(edge[1])
    print(graph)
    for key in graph.keys():
        if dfs(graph, key, set(), [], set()):
            return True
    return False 


n = 5
Edges = [[1,2],[1,3],[2,3],[2,4],[3,4],[3,5]]

# n = 5
# Edges2 = [[1,3],[3,2],[2,1],[2,4],[4,3],[3,2],[3,5]]

# n=9
# Edges = [[3,2],[3,7],[2,1],[1,7],[1,6],[6,5],[7,6],[7,5],[5,4],[8,9]]

# print("Edges1 (no cycle)",topological_order(Edges1,n))
print(topological_order(Edges,n))