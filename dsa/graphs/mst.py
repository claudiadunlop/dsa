"""Minimum spanning tree algorithms."""

from dsa.graphs.base import Graph
from typing import TypeVar, List, Set

V = TypeVar('V')
E = TypeVar('E')


def prim_mst(graph: Graph[V, E]) -> List[Graph.Edge]:
    """Compute a minimum spanning tree using Prim's algorithm.

    Prim's algorithm grows the MST one vertex at a time, always adding
    the minimum-weight edge that connects a tree vertex to a non-tree vertex.

    Assumes edge elements are numeric weights.

    Args:
        graph: An undirected, connected, weighted graph.

    Returns:
        List of edges forming a minimum spanning tree.

    Raises:
        ValueError: If the graph is directed.
    """
    raise NotImplementedError


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
        """Create a Union-Find structure with each element in its own set.

        Args:
            elements: Iterable of elements to include.
        """
        raise NotImplementedError

    def find(self, x):
        """Return the representative (root) of the set containing x.

        Uses path compression for efficiency.

        Args:
            x: An element.

        Returns:
            The representative of x's set.
        """
        raise NotImplementedError

    def union(self, x, y) -> bool:
        """Merge the sets containing x and y.

        Uses union by rank for efficiency.

        Args:
            x: An element.
            y: An element.

        Returns:
            True if x and y were in different sets (merge occurred),
            False if they were already in the same set.
        """
        raise NotImplementedError
