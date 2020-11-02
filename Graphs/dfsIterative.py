visited = set()
traversal = []

def dfsIterative(source, visited):
    dfs = []
    dfs.append(source) 
    visited.add(source) 
    while len(dfs) > 0:
        vertex = dfs.pop(0) 
        traversal.append(vertex)
        # print(vertex) 
        for v in adjList[vertex]: 
            if v not in visited:
                dfs.append(v) 
                visited.add(v)  
    
adjList = {
    'a' : ['b','c','d'],
    'b' : ['a','c'],
    'c' : ['a','b','d','e'],
    'd' : ['a','c','e'],
    'e' : ['c','d','f'],
    'f' : ['e'] 
    }

for i in adjList.keys():
    if i not in visited:
        dfsIterative(i, visited)

print(traversal)
