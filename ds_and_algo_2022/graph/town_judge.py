"""
LC: 997

ai -> bi (ai trusts bi)

town judge :
- is a sink node
- all nodes are connected to this node

cases
[] -> -1
[[1,3]] -> 3
[[3,1],[1,2],[4,5]] -> -1
[[1,3],[2,3],[4,3]] -> 3

1. construct graph/adjacency list
2. find in degree of nodes 
2. iterate in_degree keys 
    - if in_degree[key] == 0
        judge=key
3. iterate graph keys 
    - if judge not in graph[key] and key != judge:
        return -1
4. return judge
"""
import collections

class Solution:
    def construct_graph(self, n, edges):
        graph = collections.defaultdict(set)
        in_degree = collections.defaultdict(int)
        
        for i in range(1,n+1):
            graph[i] = set()
            in_degree[i] = 0
        
        for edge in edges:
            graph[edge[0]].add(edge[1])
            in_degree[edge[0]] += 1 
        return graph, in_degree 
    
    def findJudge(self, n, trust):
        graph, in_degree = self.construct_graph(n, trust) 
        judge = -1 
        
        for node in in_degree.keys():
            if in_degree[node] == 0:
                judge = node

        for key in graph.keys():
            if key != judge and judge not in graph[key]:
                return -1
        return judge

