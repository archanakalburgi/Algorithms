"""
LC : 1791

constraints: valid star graph

1. [[1,2]] -> 2

1. calculate in degree
2. iterate in_degree keys
    if in_degree[key] == len(edges)-1:
        star = key
3. return star

"""
import collections
from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        in_degree = collections.defaultdict(int)
        star = -1
        for edge in edges:
            in_degree[edge[0]]+=1
            in_degree[edge[1]]+=1
        for key in in_degree.keys():
            if in_degree[key] == len(edges):
                star = key
        return star


s = Solution()
edges = [[1,2],[5,1],[1,3],[1,4]]
print(s.findCenter(edges))
