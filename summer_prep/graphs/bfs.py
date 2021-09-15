def bfs(adj_list, source):
    queue = [source]
    visited = set()
    visited.add(source)
    traversal = []
    while queue:
        print(queue)
        vertex = queue.pop(0)
        traversal.append(vertex)
        for neighbor in adj_list[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return traversal

'''
pop(0) : [1, 2, 3, 4, 5, 6]
pop() : [1, 2, 5, 4, 3, 6] 
'''

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
print("bfs",bfs(adj_list, 'a')) 