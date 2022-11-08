"""
construct a graph from the given list of edges
"""
import typing
from typing import List
from collections import defaultdict

def construct_graph(edges:List[List[int]]) -> dict:
    graph = defaultdict(list)
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    return graph

edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
print(construct_graph(edges))