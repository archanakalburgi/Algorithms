def allPathsBetweenNodes(paths, source, destination):
    if source == destination:
        result.append(paths + [source])
    else:
        for vertex in adjList[source]:
            allPathsBetweenNodes(paths+[source], vertex, destination) 

adjList = {
    0 : [1,2],
    1 : [3,4],
    2 : [5],
    3 : [5],
    4 : [5],
    5 : []
}
result = []
allPathsBetweenNodes([], 0, 5)
print(result)   