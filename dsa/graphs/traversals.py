"""Graph traversal algorithms."""

from dsa.graphs.base import Graph
from typing import TypeVar, Dict, Set, Iterator, Optional

V = TypeVar('V')
E = TypeVar('E')


def dfs(graph: Graph[V, E], start: Graph.Vertex) -> Iterator[Graph.Vertex]:
    """Generate vertices reachable from start in depth-first order.

    Depth-first search explores as far as possible along each branch
    before backtracking.

    Args:
        graph: The graph to traverse.
        start: The starting vertex.

    Yields:
        Vertices in depth-first order.
    """
    raise NotImplementedError


def dfs_paths(graph: Graph[V, E], start: Graph.Vertex) -> Dict[Graph.Vertex, Graph.Edge]:
    """Return a dictionary mapping vertices to discovery edges.

    The discovery edges form a DFS tree rooted at start. For each
    reachable vertex v (except start), the dictionary maps v to the
    edge used to discover v.

    Args:
        graph: The graph to traverse.
        start: The starting vertex.

    Returns:
        Dictionary mapping discovered vertices to their discovery edges.
    """
    raise NotImplementedError


def bfs(graph: Graph[V, E], start: Graph.Vertex) -> Iterator[Graph.Vertex]:
    """Generate vertices reachable from start in breadth-first order.

    Breadth-first search explores all neighbors at the present depth
    before moving to vertices at the next depth level.

    Args:
        graph: The graph to traverse.
        start: The starting vertex.

    Yields:
        Vertices in breadth-first order.
    """
    raise NotImplementedError


def bfs_paths(graph: Graph[V, E], start: Graph.Vertex) -> Dict[Graph.Vertex, Graph.Edge]:
    """Return a dictionary mapping vertices to discovery edges.

    The discovery edges form a BFS tree rooted at start, which contains
    shortest paths (by number of edges) from start to each reachable vertex.

    Args:
        graph: The graph to traverse.
        start: The starting vertex.

    Returns:
        Dictionary mapping discovered vertices to their discovery edges.
    """
    raise NotImplementedError


def construct_path(start: Graph.Vertex, end: Graph.Vertex,
                   discovered: Dict[Graph.Vertex, Graph.Edge]) -> list:
    """Reconstruct path from start to end using discovered edges.

    Args:
        start: The starting vertex.
        end: The ending vertex.
        discovered: Dictionary from dfs_paths or bfs_paths.

    Returns:
        List of vertices forming the path from start to end,
        or an empty list if no path exists.
    """
    raise NotImplementedError
