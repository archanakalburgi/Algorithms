def dfs(graph, node, visited, stack):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, stack)
    stack.append(node)
    return stack


def topological_order(edges, n):
    graph = dict()

    for i in range(1, n+1):
        graph[i] = set()

    for edge in edges:
        graph[edge[0]].add(edge[1])

    visited = set()
    stack = []
    for key in graph.keys():
        if key not in visited:
            order = dfs(graph, key, visited, stack)
    return order[::-1]

n = 5
Edges = [[1,2],[1,3],[2,3],[3,4],[4,2],[3,5]]
# [1, 2, 3, 5, 4]

# n = 5
# Edges = [[1,2],[1,3],[2,3],[4,2],[3,4],[3,5]]
# # [6, 1, 2, 3, 5, 4]

# n=9
# Edges = [[3,2],[3,7],[2,1],[1,7],[1,6],[6,5],[7,6],[7,5],[5,4],[8,9]]

print(topological_order(Edges, n))