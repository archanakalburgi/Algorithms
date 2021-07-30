def get_source(in_degree):
    for key in in_degree.keys():
        if in_degree[key] == 0:
            return key
    return None

def topological_order(edges, n):
    graph = dict()
    in_degree = dict()

    for i in range(1, n+1):
        graph[i] = set()
        in_degree[i] = 0

    for edge in edges:
        graph[edge[0]].add(edge[1])
        in_degree[edge[1]] += 1 

    # print(graph)
    source = get_source(in_degree)
    queue = [source]
    order = []
    
    while queue:
        node = queue.pop(0) 
        order.append(node)
        print(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return order 

# n = 5
# Edges = [[1,2],[1,3],[2,3],[4,2],[3,4],[3,5]] # cyclic
# n=9
# Edges = [[3,2],[3,7],[2,1],[1,7],[1,6],[6,5],[7,6],[7,5],[5,4],[8,9]]
n = 5
Edges = [[1,2],[1,3],[2,3],[2,4],[3,4],[3,5]]
print(topological_order(Edges,n)) 


'''
for detecting cycle :

if len(in_degree) != len(order) : cyclic

if source not found : cyclic 
if source != None:
    queue = [source]

'''