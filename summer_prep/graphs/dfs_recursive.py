def dfs_recursive(adj_list, source, visited, traversal):
    traversal.append(source)
    for neighbor in adj_list[source]:
        if neighbor not in visited:
            visited.add(neighbor)
            dfs_recursive(adj_list, neighbor, visited, traversal)

    return traversal

adj_list = {'A':['B','C'],
'B':['D','E'],
'C':['F'],
'D' : [],
'E':['F'], 
'F':[]}

print(dfs_recursive(adj_list, 'A', set('A'), []))