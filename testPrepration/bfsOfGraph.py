def breadthFirstTravelsal(source):
    visited = set()
    traversal = []
    queue = []

    visited.add(source)
    queue.append(source)

    while queue:
        node = queue.pop(0)
        traversal.append(node) 
        for vertex in adjList[node]: 
            if vertex not in visited:
                visited.add(vertex)
                queue.append(vertex)

    return traversal

adjList = {
    'a' : ['b','c','d'],
    'b' : ['c'],
    'c' : ['b','d','e'],
    'd' : ['a','c','e'],
    'e' : ['c','d','f'],
    'f' : [] 
    }

source = 'a'

print(breadthFirstTravelsal(source))