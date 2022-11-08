"""
LC 1971. Find if Path Exists in Graph
"""
from collections import defaultdict
from typing import List

class Solution:
    def __init__(self):
        self.visited = set()
        self.graph = defaultdict(list)

    def construct_graph(self, edges: List[List[int]]) -> None:          
        for edge in edges:
            self.graph[edge[0]].append(edge[1]) 
            self.graph[edge[1]].append(edge[0])

    def dfs(self, source, destination)-> bool:
        if source == destination:
            return True
        if source not in self.visited:
            self.visited.add(source)
            for neighbor in self.graph[source]:
                if self.dfs(neighbor, destination):
                    return True
            return False

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.construct_graph(edges)
        return self.dfs(source, destination)


sol = Solution()
n = 10
edges = [[4,3],[1,4],[4,8],[1,7],[6,4],[4,2],[7,4],[4,0],[0,9],[5,4]]
source = 5
destination = 9
assert (sol.validPath(n, edges, source, destination)==True) 