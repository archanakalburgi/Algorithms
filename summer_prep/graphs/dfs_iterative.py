def dfs_iterative(adj_list, source, visited, traversal):
    stack = [source]
    visited.add(source)

    while stack:
        print(stack)
        vertex = stack.pop() # vertex = queue.pop(0)
        traversal.append(vertex)
        for neighbor in adj_list[vertex]: 
            if neighbor not in adj_list.keys():
                adj_list[neighbor] = []
            if neighbor not in visited:
                stack.append(neighbor) 
                visited.add(neighbor)
            # print(stack)
    return traversal 

# adj_list = {1 : [2,3],
# 2 : [1],
# 3 : [1],
# 4 : [5],
# 5 : [4]} 

# adj_list = {1:[2],
# 2:[1,3,4,5],
# 3:[2,6],
# 4:[2],
# 5:[2],
# 6:[3]}

adj_list = {
    'a' : ['b'],
    'b' : ['a','f','e','c'],
    'c' : ['b','d'],
    'd' : ['c'],
    'e' : ['b'],
    'f' : ['b']
}

'''[1, 2, 5, 4, 3, 6]'''
visited = set()
print("dfs",dfs_iterative(adj_list, 'a', visited, []))