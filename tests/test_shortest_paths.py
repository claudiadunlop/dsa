"""Tests for shortest path algorithms."""

import pytest
from dsa.graphs.adjacency_map import AdjacencyMapGraph
from dsa.graphs.shortest_paths import dijkstra, shortest_path, bellman_ford


def build_weighted_graph():
    """Build a sample weighted directed graph for testing.

    Graph structure (edge weights shown):
        A --1--> B --2--> C
        |        |        |
        v        v        v
        4        1        3
        |        |        |
        v        v        v
        D --2--> E --1--> F

    Shortest paths from A:
        A -> A: 0
        A -> B: 1
        A -> C: 3
        A -> D: 4
        A -> E: 2
        A -> F: 3
    """
    g = AdjacencyMapGraph(directed=True)
    vertices = {}
    for name in "ABCDEF":
        vertices[name] = g.insert_vertex(name)

    g.insert_edge(vertices["A"], vertices["B"], 1)
    g.insert_edge(vertices["B"], vertices["C"], 2)
    g.insert_edge(vertices["A"], vertices["D"], 4)
    g.insert_edge(vertices["B"], vertices["E"], 1)
    g.insert_edge(vertices["C"], vertices["F"], 3)
    g.insert_edge(vertices["D"], vertices["E"], 2)
    g.insert_edge(vertices["E"], vertices["F"], 1)

    return g, vertices


class TestDijkstra:
    """Tests for Dijkstra's algorithm."""

    def test_single_vertex(self):
        g = AdjacencyMapGraph(directed=True)
        v = g.insert_vertex("A")
        distances, predecessors = dijkstra(g, v)
        assert distances[v] == 0
        assert v not in predecessors

    def test_two_vertices(self):
        g = AdjacencyMapGraph(directed=True)
        u = g.insert_vertex("A")
        v = g.insert_vertex("B")
        g.insert_edge(u, v, 5)
        distances, predecessors = dijkstra(g, u)
        assert distances[u] == 0
        assert distances[v] == 5

    def test_sample_graph(self):
        g, vertices = build_weighted_graph()
        distances, predecessors = dijkstra(g, vertices["A"])
        assert distances[vertices["A"]] == 0
        assert distances[vertices["B"]] == 1
        assert distances[vertices["C"]] == 3
        assert distances[vertices["D"]] == 4
        assert distances[vertices["E"]] == 2
        assert distances[vertices["F"]] == 3

    def test_unreachable_vertex(self):
        g = AdjacencyMapGraph(directed=True)
        u = g.insert_vertex("A")
        v = g.insert_vertex("B")  # No edge from A to B
        distances, predecessors = dijkstra(g, u)
        assert distances[u] == 0
        assert distances.get(v, float('inf')) == float('inf')

    def test_negative_weight_raises(self):
        g = AdjacencyMapGraph(directed=True)
        u = g.insert_vertex("A")
        v = g.insert_vertex("B")
        g.insert_edge(u, v, -1)
        with pytest.raises(ValueError):
            dijkstra(g, u)


class TestShortestPath:
    """Tests for shortest path reconstruction."""

    def test_path_exists(self):
        g, vertices = build_weighted_graph()
        distance, path = shortest_path(g, vertices["A"], vertices["F"])
        assert distance == 3
        elements = [v.element() for v in path]
        assert elements[0] == "A"
        assert elements[-1] == "F"

    def test_no_path(self):
        g = AdjacencyMapGraph(directed=True)
        u = g.insert_vertex("A")
        v = g.insert_vertex("B")
        distance, path = shortest_path(g, u, v)
        assert distance == float('inf')
        assert path == []

    def test_same_vertex(self):
        g = AdjacencyMapGraph(directed=True)
        v = g.insert_vertex("A")
        distance, path = shortest_path(g, v, v)
        assert distance == 0
        assert len(path) == 1
        assert path[0].element() == "A"


class TestBellmanFord:
    """Tests for Bellman-Ford algorithm."""

    def test_single_vertex(self):
        g = AdjacencyMapGraph(directed=True)
        v = g.insert_vertex("A")
        distances, predecessors = bellman_ford(g, v)
        assert distances[v] == 0

    def test_sample_graph(self):
        g, vertices = build_weighted_graph()
        distances, predecessors = bellman_ford(g, vertices["A"])
        assert distances[vertices["A"]] == 0
        assert distances[vertices["B"]] == 1
        assert distances[vertices["C"]] == 3
        assert distances[vertices["E"]] == 2
        assert distances[vertices["F"]] == 3

    def test_negative_weights(self):
        """Bellman-Ford should handle negative weights."""
        g = AdjacencyMapGraph(directed=True)
        a = g.insert_vertex("A")
        b = g.insert_vertex("B")
        c = g.insert_vertex("C")
        g.insert_edge(a, b, 4)
        g.insert_edge(a, c, 2)
        g.insert_edge(c, b, -3)  # Negative edge
        distances, _ = bellman_ford(g, a)
        assert distances[a] == 0
        assert distances[b] == -1  # Via A -> C -> B
        assert distances[c] == 2

    def test_negative_cycle_raises(self):
        """Bellman-Ford should detect negative cycles."""
        g = AdjacencyMapGraph(directed=True)
        a = g.insert_vertex("A")
        b = g.insert_vertex("B")
        c = g.insert_vertex("C")
        g.insert_edge(a, b, 1)
        g.insert_edge(b, c, -1)
        g.insert_edge(c, a, -1)  # Creates negative cycle
        with pytest.raises(ValueError):
            bellman_ford(g, a)
