def dfs(source):
    dfsPath = []
    stack.append(source) 
    visited.add(source)
    while stack:
        node = stack.pop() 
        dfsPath.append(node) 
        for vertex in adjList[node]:
            if vertex not in visited:
                visited.add(vertex)
                stack.append(vertex)
    return dfsPath
    
        
adjList = {
    0 : [1,3],
    1 : [0,2],
    2 : [0,3],
    3 : [0,2],
    4 : [5],
    5 : [4,6],
    6 : [5]
}
visited = set()
stack = []

for v in adjList.keys(): 
    if v not in visited: 
        print(dfs(v))  