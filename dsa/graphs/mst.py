"""Minimum spanning tree algorithms."""

from dsa.graphs.base import Graph
from typing import TypeVar, List, Set

V = TypeVar('V')
E = TypeVar('E')


def kruskal_mst(graph: Graph[V, E]) -> List[Graph.Edge]:
    """Compute a minimum spanning tree using Kruskal's algorithm.

    Kruskal's algorithm builds the MST by considering edges in order of
    increasing weight, adding each edge that doesn't create a cycle.

    Assumes edge elements are numeric weights.

    Args:
        graph: An undirected, connected, weighted graph.

    Returns:
        List of edges forming a minimum spanning tree.

    Raises:
        ValueError: If the graph is directed.
    """
    raise NotImplementedError

class UnionFind:
    """Union-Find (Disjoint Set Union) data structure.
    Supports efficient union and find operations for use in Kruskal's
    algorithm to detect cycles.
    """
    def __init__(self, elements):
        self.parent = {x: x for x in elements}
        self.rank = {x: 0 for x in elements}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y) -> bool:
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True
