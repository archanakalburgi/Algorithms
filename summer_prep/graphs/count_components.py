def dfs_iterative(adj_list, source, visited, traversal):
    stack = [source]
    visited.add(source)

    while stack:
        # print(stack)
        vertex = stack.pop() # vertex = queue.pop(0)
        traversal.append(vertex)
        # print("traversal",traversal)
        for neighbor in adj_list[vertex]: 
            if neighbor not in adj_list.keys():
                adj_list[neighbor] = []
            if neighbor not in visited:
                stack.append(neighbor) 
                visited.add(neighbor)
    return traversal 

adj_list = {1 : [2,3],
2 : [1],
3 : [1],
4 : [5],
5 : [4]} 

# traversal = []
visited = set()
count = 0

for node in adj_list.keys():
    if node not in visited:
        traversal = []
        dfs_iterative(adj_list, node, visited,traversal)
        print(traversal)
        count += 1

print(count) 