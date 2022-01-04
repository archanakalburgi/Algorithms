def get_source(indegree):
    for key in indegree.keys():
        if indegree[key] == 0:
            return key
    return None 

def topo_sort(edges,n):
    graph = dict()
    indegree = dict()
    order = list()

    for i in range(1,n+1):
        graph[i] = set()
        indegree[i] = 0

    for edge in edges:
        graph[edge[0]] = edge[1]
        indegree[edge[1]] += 1 
    
    if get_source(indegree) == None:
        return True
    else:
        queue = [get_source(indegree)] 

    while queue:
        node = queue.pop(0)
        order.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -=1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(order) != len(graph.keys()):
        return True 
    return False

n=9
Edges = [[1,2],[2,3],[3,1]] 
print(topo_sort(Edges,n)) 