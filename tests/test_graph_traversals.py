"""Tests for graph traversal algorithms."""

import pytest
from dsa.graphs.adjacency_map import AdjacencyMapGraph
from dsa.graphs.traversals import dfs, bfs, dfs_paths, bfs_paths, construct_path


def build_sample_graph():
    """Build a sample undirected graph for testing.

    Graph structure:
        A --- B --- C
        |     |
        D --- E --- F
    """
    g = AdjacencyMapGraph(directed=False)
    vertices = {}
    for name in "ABCDEF":
        vertices[name] = g.insert_vertex(name)

    g.insert_edge(vertices["A"], vertices["B"])
    g.insert_edge(vertices["B"], vertices["C"])
    g.insert_edge(vertices["A"], vertices["D"])
    g.insert_edge(vertices["B"], vertices["E"])
    g.insert_edge(vertices["D"], vertices["E"])
    g.insert_edge(vertices["E"], vertices["F"])

    return g, vertices


class TestDFS:
    """Tests for depth-first search."""

    def test_single_vertex(self):
        g = AdjacencyMapGraph()
        v = g.insert_vertex("A")
        result = list(dfs(g, v))
        assert len(result) == 1
        assert result[0].element() == "A"

    def test_visits_all_connected(self):
        g, vertices = build_sample_graph()
        result = list(dfs(g, vertices["A"]))
        elements = {v.element() for v in result}
        assert elements == {"A", "B", "C", "D", "E", "F"}

    def test_disconnected_graph(self):
        g = AdjacencyMapGraph()
        v1 = g.insert_vertex("A")
        v2 = g.insert_vertex("B")
        g.insert_vertex("C")  # Disconnected
        g.insert_edge(v1, v2)
        result = list(dfs(g, v1))
        elements = {v.element() for v in result}
        assert elements == {"A", "B"}


class TestBFS:
    """Tests for breadth-first search."""

    def test_single_vertex(self):
        g = AdjacencyMapGraph()
        v = g.insert_vertex("A")
        result = list(bfs(g, v))
        assert len(result) == 1
        assert result[0].element() == "A"

    def test_visits_all_connected(self):
        g, vertices = build_sample_graph()
        result = list(bfs(g, vertices["A"]))
        elements = {v.element() for v in result}
        assert elements == {"A", "B", "C", "D", "E", "F"}

    def test_level_order(self):
        """BFS should visit vertices in level order from start."""
        g, vertices = build_sample_graph()
        result = list(bfs(g, vertices["A"]))
        elements = [v.element() for v in result]
        # A should be first
        assert elements[0] == "A"
        # B and D are at distance 1 from A
        assert set(elements[1:3]) == {"B", "D"}


class TestPaths:
    """Tests for path construction."""

    def test_dfs_paths(self):
        g, vertices = build_sample_graph()
        discovered = dfs_paths(g, vertices["A"])
        # Start vertex should not be in discovered
        assert vertices["A"] not in discovered
        # All other vertices should be discovered
        for name in "BCDEF":
            assert vertices[name] in discovered

    def test_bfs_paths(self):
        g, vertices = build_sample_graph()
        discovered = bfs_paths(g, vertices["A"])
        assert vertices["A"] not in discovered
        for name in "BCDEF":
            assert vertices[name] in discovered

    def test_construct_path(self):
        g, vertices = build_sample_graph()
        discovered = bfs_paths(g, vertices["A"])
        path = construct_path(vertices["A"], vertices["F"], discovered)
        elements = [v.element() for v in path]
        # Path should start at A and end at F
        assert elements[0] == "A"
        assert elements[-1] == "F"
        # BFS gives shortest path: A-B-E-F or A-D-E-F (both length 4)
        assert len(path) == 4

    def test_no_path(self):
        g = AdjacencyMapGraph()
        v1 = g.insert_vertex("A")
        v2 = g.insert_vertex("B")  # Disconnected
        discovered = bfs_paths(g, v1)
        path = construct_path(v1, v2, discovered)
        assert path == []
