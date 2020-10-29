from queue import Queue

def bfs(adjList, source):
    visited = set() # {} so that we dont revisit the same node 
    bfsTraversal = []  
    queue = Queue() # we want to know where to go next

    visited.add(source) 
    queue.put(source)
   

    while queue.qsize() > 0: # queue onj is never empty. so check if size of queue > 0
        node = queue.get() 
        bfsTraversal.append(node)                                                     
        # print(adjList[node])
    
        for k in adjList[node]:  # adj[a] = [b,c,d] , k = b 
            if k not in visited:
                visited.add(k)
                queue.put(k) 
    
    print(bfsTraversal)  

adjList = {
    'a' : ['c','b','d'],
    'b' : ['a','c'],
    'c' : ['a','b','d','e'],
    'd' : ['a','c','e'],
    'e' : ['c','d','f'],
    'f' : ['e'] 
    }

source = 'a'

bfs(adjList, source)