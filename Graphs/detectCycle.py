def dfs(source):
    visited.add(source)

    for v in adjList[source]:
        if v not in visited:
            return dfs(v)
        elif v in visited:
            return True 
            
adjList = {
    0 : [1],
    1 : [2],
    2 : [0] 
} 

visited = set() 

if dfs(0):
    print('True')
else:
    print('False')  
