adjList = {
    0 : [1,3],
    1 : [0,2],
    2 : [1,3],
    3 : [0,2],
    4 : [5],
    5 : [4,6],
    6 : [5]
}
visited = set()
dfs = []
components = []

def connectedComponents(adjList, source):
    visited.add(source)
    dfs.append(source)
    for vertex in adjList[source]:
        if vertex not in visited:
            connectedComponents(adjList, vertex) 

for key in adjList.keys():
    if key not in visited:
        dfs = []
        connectedComponents(adjList, key) 
        components.append(dfs)

print(components) 