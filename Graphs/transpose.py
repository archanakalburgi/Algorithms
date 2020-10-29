'''
You have to implement a function which will take a graph as input and print its transpose.

Input # A graph

adjList = {
    0 : 1,2
    1 : 3,4
    2 : 
    3 : 
    4 :
}
            
            0
          /   \
         .     .
         1     2
        / \
       .   .  
       3   4

Output :

adjList = {
    0 : 
    1 : 0
    2 : 0
    3 : 1
    4 : 1
}

            0
          .   .
        /       \
       1         2
      .  .
    /      \
   3        4 

'''

adjList = {
    0 : 1,2
    1 : 3,4
    2 : 
    3 : 
    4 :
} 
visited = set() 
newAdjList = {}

def dfs(source):

    visited.add(source) 
    for vertex in adjList[source]: # exploring adjacent vertex of source 
        if vertex not in visited:
            dfs(vertex) 