def count_sink_nodes(n, edges):
    graph = dict()
    for i in range(1,n+1):
        graph[i] = []
    
    for edge in edges:
        graph[edge[0]].append(edge[1])

    print(graph)
    count = 0
    for key in graph.keys():
        if len(graph[key]) == 0:
            count += 1
    
    return count 


n = 4
m = 2
Edges = [[2, 3], [4, 3]] 

print(count_sink_nodes(n, Edges)) 