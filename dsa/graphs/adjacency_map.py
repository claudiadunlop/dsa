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
            return self._element
            #raise NotImplementedError

        def __eq__(self, other: object) -> bool:
            return self is other
            #raise NotImplementedError

        def __hash__(self) -> int:
            return hash(id(self))
            #raise NotImplementedError

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
            return self._element
            #raise NotImplementedError

        def endpoints(self) -> Tuple[Graph.Vertex, Graph.Vertex]:
            return (self._origin, self._destination)
            #raise NotImplementedError

        def opposite(self, v: Graph.Vertex) -> Graph.Vertex:
            return self._destination if v is self._origin else self._origin
            #raise NotImplementedError

        def __eq__(self, other: object) -> bool:
            return self is other
            #raise NotImplementedError

        def __hash__(self) -> int:
            return hash( (self._origin, self._destination) )
            #raise NotImplementedError

    def __init__(self, directed: bool = False):
        """Create an empty graph.

        Args:
            directed: True for a directed graph, False for undirected.
        """
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing
        #raise NotImplementedError

    def is_directed(self) -> bool:
        return self._incoming is not self._outgoing
        #raise NotImplementedError

    def vertex_count(self) -> int:
        return len(self._outgoing)
        #raise NotImplementedError

    def edge_count(self) -> int:
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        return total if self.is_directed() else total // 2
        #raise NotImplementedError

    def vertices(self) -> Iterator[Graph.Vertex]:
        return self._outgoing.keys()
        #raise NotImplementedError

    def edges(self) -> Iterator[Graph.Edge]:
        result = set()
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())
        return result
        #raise NotImplementedError

    def get_edge(self, u: Graph.Vertex, v: Graph.Vertex) -> Optional[Graph.Edge]:
        return self._outgoing[u].get(v)
        #raise NotImplementedError

    def degree(self, v: Graph.Vertex, outgoing: bool = True) -> int:
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])
        #raise NotImplementedError

    def incident_edges(self, v: Graph.Vertex, outgoing: bool = True) -> Iterator[Graph.Edge]:
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge
        #raise NotImplementedError

    def insert_vertex(self, x: V = None) -> Graph.Vertex:
        v = self._Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}
        return v
        #raise NotImplementedError

    def insert_edge(self, u: Graph.Vertex, v: Graph.Vertex, x: E = None) -> Graph.Edge:
        e = self._Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e
        return e
        #raise NotImplementedError

    def remove_vertex(self, v: Graph.Vertex) -> V:
        for u in list(self._outgoing[v]):
            del self._incoming[u][v]
        del self._outgoing[v]
        if self.is_directed():
            for u in list(self._incoming[v]):
                del self._outgoing[u][v]
            del self._incoming[v]

        return v.element()
        #raise NotImplementedError

    def remove_edge(self, e: Graph.Edge) -> E:
        u, v = e.endpoints()
        del self._outgoing[u][v]
        del self._incoming[v][u]
        return e.element()
        #raise NotImplementedError
