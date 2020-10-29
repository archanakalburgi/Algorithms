'''
Input # A graph represented as an adjacency list and a starting vertex 
Output # A string containing the vertices of the graph listed in the correct order of traversal 
'''

adjList = {
    0 : [1,2],
    1 : [3,4],
    2 : [],
    3 : [],
    4 : []
    }

visited = set()
dfsTraversal = ''
temp = ''
def dfs(source, dfsTraversal): # dfs(0, '') , (1, '0'), (3,'01'), (4, '01') 
    visited.add(source) # visited = (0,1,3,4)
    dfsTraversal = dfsTraversal + str(source)   # dfsT = '0' , dfsT = '01' , '013' , '014'
    
    for vertex in adjList[source]: # vertex = 1, 3, none, 4, 2 
        if vertex not in visited: # true, true , true  
            dfs(vertex, dfsTraversal) # (1,'0'), (3, '01'), (4,'01,),
    print(dfsTraversal) 
    # print(type(dfsTraversal))
    
dfs(0, dfsTraversal) 

'''
visited = set()
 
def dfs(source):
    dfsTraversal = ''

    visited.add(source)
    dfsTraversal = dfsTraversal + str(source)  # '' + 0 

    for vertex in adjList[source]: 
        if vertex not in visited:
            dfs(vertex)
    print(dfsTraversal)
    
dfs(0)
 
3
4
2
1
0 
'''