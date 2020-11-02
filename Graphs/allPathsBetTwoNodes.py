'''
Implement a function that prints all paths that exist between two nodes (source to destination).

Input # A graph, a source value, and a destination value source = 0 destination = 5

Output # A 2D list having all path 
'''

def allPaths(path, source, destination):
    if source == destination:
        return result.append(path + [destination])  
    
    else:
        for vertex in adjList[source]: 
            allPaths(path+[source], vertex, 5)   

    
adjList = {
    0 : [1,2],
    1 : [3,4],
    2 : [5],
    3 : [5],
    4 : [5],
    5 : []
}
result = []
allPaths([], 0, 5)  
print(result)  