"""Adjacency map implementation of a graph."""

from dsa.graphs.base import Graph
from typing import TypeVar, Iterator, Optional, Tuple

V = TypeVar('V')
E = TypeVar('E')


class AdjacencyMapGraph(Graph[V, E]):
    """Graph implementation using an adjacency map.

    Each vertex maintains a dictionary mapping adjacent vertices to
    the edges connecting them. This provides O(1) edge lookup between
    any two vertices.

    Supports both directed and undirected graphs.
    """

    class _Vertex(Graph.Vertex):
        """Vertex implementation for AdjacencyMapGraph."""
        __slots__ = '_element'

        def __init__(self, element: V):
            self._element = element

        def element(self) -> V:
            raise NotImplementedError

        def __eq__(self, other: object) -> bool:
            raise NotImplementedError

        def __hash__(self) -> int:
            raise NotImplementedError

    class _Edge(Graph.Edge):
        """Edge implementation for AdjacencyMapGraph."""
        __slots__ = '_element', '_origin', '_destination'

        def __init__(self, origin: 'AdjacencyMapGraph._Vertex',
                     destination: 'AdjacencyMapGraph._Vertex',
                     element: E):
            self._element = element
            self._origin = origin
            self._destination = destination

        def element(self) -> E:
            raise NotImplementedError

        def endpoints(self) -> Tuple[Graph.Vertex, Graph.Vertex]:
            raise NotImplementedError

        def opposite(self, v: Graph.Vertex) -> Graph.Vertex:
            raise NotImplementedError

        def __eq__(self, other: object) -> bool:
            raise NotImplementedError

        def __hash__(self) -> int:
            raise NotImplementedError

    def __init__(self, directed: bool = False):
        """Create an empty graph.

        Args:
            directed: True for a directed graph, False for undirected.
        """
        raise NotImplementedError

    def is_directed(self) -> bool:
        raise NotImplementedError

    def vertex_count(self) -> int:
        raise NotImplementedError

    def edge_count(self) -> int:
        raise NotImplementedError

    def vertices(self) -> Iterator[Graph.Vertex]:
        raise NotImplementedError

    def edges(self) -> Iterator[Graph.Edge]:
        raise NotImplementedError

    def get_edge(self, u: Graph.Vertex, v: Graph.Vertex) -> Optional[Graph.Edge]:
        raise NotImplementedError

    def degree(self, v: Graph.Vertex, outgoing: bool = True) -> int:
        raise NotImplementedError

    def incident_edges(self, v: Graph.Vertex, outgoing: bool = True) -> Iterator[Graph.Edge]:
        raise NotImplementedError

    def insert_vertex(self, x: V = None) -> Graph.Vertex:
        raise NotImplementedError

    def insert_edge(self, u: Graph.Vertex, v: Graph.Vertex, x: E = None) -> Graph.Edge:
        raise NotImplementedError

    def remove_vertex(self, v: Graph.Vertex) -> V:
        raise NotImplementedError

    def remove_edge(self, e: Graph.Edge) -> E:
        raise NotImplementedError
