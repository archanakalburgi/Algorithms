def dfs_recursive(adj_list, source, visited, traversal):
    traversal.append(source)
    for neighbor in adj_list[source]:
        if neighbor in visited:
            return True
        if neighbor not in visited:
            visited.add(neighbor)
            dfs_recursive(adj_list, neighbor, visited, traversal)

    return False

# adj_list = {1 : [2,3],
# 2 : [1,3],
# 3 : [1,2],
# 4 : [5],
# 5 : [4]}

adj_list = {
    'a' : ['b'],
    'b' : ['a','f','e','c'],
    'c' : ['b','d'],
    'd' : ['c'],
    'e' : ['b'],
    'f' : ['b']
}

print(dfs_recursive(adj_list, 'a', set(), []))