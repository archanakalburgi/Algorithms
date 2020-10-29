'''
vertices :

adjList = {
    'a' : ['b','c','d'],
    'b' : ['a','c'],
    'c' : ['a','b','d','e'],
    'd' : ['a','c','e'],
    'e' : ['c','d','f'],
    'f' : ['e'] 
    }

all the edges 

edges = [
    ('a','b'),
    ('a','d'),
    ('a','c'),
    ('b','c'),
    ('c','d'),
    ('c','e'),
    ('d','e'),
    ('e','f')
]

adjMatrix = [
    [1,1,1,1,0,0],  
    [1,1,1,0,0,0],
    [1,1,1,1,1,0],
    [1,0,1,1,1,0],
    [0,0,1,1,1,1],
    [0,0,0,0,1,1]
]
''' 

class Graph(): 
    def __init__(self): # initialize vertices and adjacency list (an empty dictionary)
        self.vertices = vertices 
        self.adjList = {}

        # adding all vertices to the dictionary  
        for vertex in self.vertices: 
            self.adjList[vertex] =  [] 

    # creating/ initialising edges of the graph 
    def addEdges(self, vertex, neighbour):
        self.adjList[vertex].append(neighbour)
        self.adjList[neighbour].append(vertex)  

    def printAdjList(self, vertices):
        for vertex in vertices:
            print(vertex , '->', self.adjList[vertex])  
        

vertices = ['a','b','c','d','e','f']

edges = [
    ('a','b'),
    ('a','d'),
    ('a','c'),
    ('b','c'),
    ('c','d'),
    ('c','e'),
    ('d','e'),
    ('e','f')
]

graph = Graph() 

for v, n in edges:
    graph.addEdges(v,n) 

graph.printAdjList(vertices)
