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

def dfs(source, paths): 
    if source == len(adjList)-1 :
        return dfsTraversal.append(str(paths + str(source)))   
    
    for vertex in adjList[source]: 
        dfs(vertex, ''.join(paths + str(source))) 

dfsTraversal = []
dfs(0, '') 
# print(dfsTraversal)
print(','.join(dfsTraversal)) 

'''
output : 014 
as per prob only one path to traverse the graph 
'''  