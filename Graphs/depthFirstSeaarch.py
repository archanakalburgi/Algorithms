adjList = {
    'a' : ['b','c','d'],
    'b' : ['a','c'],
    'c' : ['a','b','d','e'],
    'd' : ['a','c','e'],
    'e' : ['c','d','f'],
    'f' : ['e'] 
    }

'''
visited = {a:1}
# parent = {}
dfsTraversal = [] 

for node in adjList.keys():
    visited[node] = 0 
#     # parent[node] = None

def dfs(source):

    visited[source] = 1
    dfsTraversal.append(source)

    for vertex in adjList[source]: # exploring adjacent vertex of source 
        if visited[vertex] == 0:
            # parent[vertex] = source
            dfs(vertex) 
   
dfs('a')  
print(dfsTraversal)

'''


visited = set()
dfsTraversal = [] 

def dfs(source):

    visited.add(source)
    dfsTraversal.append(source)

    for vertex in adjList[source]: # exploring adjacent vertex of source 
        if vertex not in visited:
            dfs(vertex) 
   
dfs('a')  
print(dfsTraversal) 

