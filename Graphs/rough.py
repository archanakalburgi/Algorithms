def dfs(source):
    stack.append(source) 
    visited.add(source)
    # print(source) 
    while stack:
        node = stack.pop() 
        dfsPath.append(node) 
        for vertex in adjList[node]:
            if vertex not in visited:
                visited.add(vertex)
                stack.append(vertex)
    # print(visited)
    # print(stack)
    
adjList = {
    'a' : ['b','c','d'],
    'b' : ['a','c'],
    'c' : ['a','b','d','e'],
    'd' : ['a','c','e'],
    'e' : ['c','d','f'],
    'f' : ['e'] 
    }

visited = set()
stack = []
dfsPath = []
for v in adjList.keys(): 
    if v not in visited:
        dfs(v)     

print(dfsPath)