"""Abstract base class defining the graph interface."""

from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Iterator, Optional, Tuple

V = TypeVar('V')  # Vertex element type
E = TypeVar('E')  # Edge element type


class Graph(ABC, Generic[V, E]):
    """Abstract base class for a graph structure.

    A graph consists of vertices (nodes) and edges connecting pairs of
    vertices. This interface supports both directed and undirected graphs.

    The graph uses a vertex/edge abstraction where vertices and edges
    are represented by opaque objects that store elements.

    Core operations and their expected time complexities
    (for adjacency map representation):
        vertex_count()          - Return number of vertices     O(1)
        edge_count()            - Return number of edges        O(1)
        vertices()              - Iterate over all vertices     O(n)
        edges()                 - Iterate over all edges        O(m)
        get_edge(u, v)          - Return edge from u to v       O(1)
        degree(v)               - Return degree of vertex       O(1)
        incident_edges(v)       - Iterate edges incident to v   O(deg(v))
        insert_vertex(x)        - Add new vertex with element x O(1)
        insert_edge(u, v, x)    - Add edge from u to v          O(1)
        remove_vertex(v)        - Remove vertex v               O(deg(v))
        remove_edge(e)          - Remove edge e                 O(1)

    where n = number of vertices, m = number of edges.
    """

    class Vertex(ABC):
        """An abstraction for a graph vertex."""

        @abstractmethod
        def element(self) -> V:
            """Return the element stored at this vertex."""
            pass

        @abstractmethod
        def __eq__(self, other: object) -> bool:
            """Return True if other represents the same vertex."""
            pass

        @abstractmethod
        def __hash__(self) -> int:
            """Return hash code for this vertex (for use in sets/dicts)."""
            pass

    class Edge(ABC):
        """An abstraction for a graph edge."""

        @abstractmethod
        def element(self) -> E:
            """Return the element stored at this edge."""
            pass

        @abstractmethod
        def endpoints(self) -> Tuple['Graph.Vertex', 'Graph.Vertex']:
            """Return (u, v) tuple for vertices u and v connected by this edge."""
            pass

        @abstractmethod
        def opposite(self, v: 'Graph.Vertex') -> 'Graph.Vertex':
            """Return the vertex opposite to v on this edge.

            Raises:
                ValueError: If v is not an endpoint of this edge.
            """
            pass

        @abstractmethod
        def __eq__(self, other: object) -> bool:
            """Return True if other represents the same edge."""
            pass

        @abstractmethod
        def __hash__(self) -> int:
            """Return hash code for this edge (for use in sets/dicts)."""
            pass

    @abstractmethod
    def is_directed(self) -> bool:
        """Return True if the graph is directed, False if undirected."""
        pass

    @abstractmethod
    def vertex_count(self) -> int:
        """Return the number of vertices in the graph."""
        pass

    @abstractmethod
    def edge_count(self) -> int:
        """Return the number of edges in the graph."""
        pass

    @abstractmethod
    def vertices(self) -> Iterator[Vertex]:
        """Return an iteration of all vertices in the graph."""
        pass

    @abstractmethod
    def edges(self) -> Iterator[Edge]:
        """Return an iteration of all edges in the graph."""
        pass

    @abstractmethod
    def get_edge(self, u: Vertex, v: Vertex) -> Optional[Edge]:
        """Return the edge from u to v, or None if not adjacent.

        For an undirected graph, get_edge(u, v) == get_edge(v, u).
        For a directed graph, this returns the edge from u to v only.

        Args:
            u: Origin vertex.
            v: Destination vertex.

        Returns:
            The edge from u to v, or None if no such edge exists.
        """
        pass

    @abstractmethod
    def degree(self, v: Vertex, outgoing: bool = True) -> int:
        """Return the number of edges incident to vertex v.

        For an undirected graph, this is the total degree.
        For a directed graph:
            - If outgoing=True, return out-degree (edges leaving v)
            - If outgoing=False, return in-degree (edges entering v)

        Args:
            v: The vertex.
            outgoing: For directed graphs, whether to count outgoing edges.

        Returns:
            The degree of the vertex.
        """
        pass

    @abstractmethod
    def incident_edges(self, v: Vertex, outgoing: bool = True) -> Iterator[Edge]:
        """Return all edges incident to vertex v.

        For an undirected graph, this returns all edges touching v.
        For a directed graph:
            - If outgoing=True, return edges leaving v
            - If outgoing=False, return edges entering v

        Args:
            v: The vertex.
            outgoing: For directed graphs, whether to return outgoing edges.

        Yields:
            Edges incident to v.
        """
        pass

    @abstractmethod
    def insert_vertex(self, x: V = None) -> Vertex:
        """Insert and return a new vertex with element x.

        Args:
            x: The element to store at the new vertex.

        Returns:
            The newly created vertex.
        """
        pass

    @abstractmethod
    def insert_edge(self, u: Vertex, v: Vertex, x: E = None) -> Edge:
        """Insert and return a new edge from u to v with element x.

        Args:
            u: Origin vertex.
            v: Destination vertex.
            x: The element to store at the new edge.

        Returns:
            The newly created edge.

        Raises:
            ValueError: If u and v are not vertices of this graph.
            ValueError: If u and v are already adjacent.
        """
        pass

    @abstractmethod
    def remove_vertex(self, v: Vertex) -> V:
        """Remove vertex v and all incident edges, returning stored element.

        Args:
            v: The vertex to remove.

        Returns:
            The element that was stored at v.
        """
        pass

    @abstractmethod
    def remove_edge(self, e: Edge) -> E:
        """Remove edge e and return its stored element.

        Args:
            e: The edge to remove.

        Returns:
            The element that was stored at e.
        """
        pass
