"""
LC : 841

1. [[1]] -> true
2. [[1],[3]] -> false
3. [[1,3],[3,0,1],[2],[0]] -> false

{   0 : 1,3,
    1: 3,0,1,
    2: 2,
    3: 0
}

1. construct graph
2. dfs path
3 if len(path) == len(rooms)-1:
    return true
return false
"""
import collections

class Solution:
    def __init__(self):
        self.visited = set()
        self.graph = collections.defaultdict(list)

    def construct_graph(self, edges):
        for i in range(len(edges)):
            self.graph[i]=edges[i]
        return self.graph

    def dfs(self, source, path):
        path.append(source)
        for neighbor in self.graph[source]:
            if neighbor not in self.visited:
                self.visited.add(neighbor)
                self.dfs(neighbor, path)
        return path 
            
    def canVisitAllRooms(self, rooms):
        self.construct_graph(rooms)
        dfs_path = self.dfs(0, [])
        if len(set(dfs_path)) == len(rooms):
            return True
        return False 