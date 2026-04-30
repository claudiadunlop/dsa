"""Tests for minimum spanning tree algorithms."""

import pytest
from dsa.graphs.adjacency_map import AdjacencyMapGraph
from dsa.graphs.mst import kruskal_mst, UnionFind


def build_weighted_graph():
    """Build a sample weighted undirected graph for testing.

    Graph structure (edge weights shown):
        A --4-- B --8-- C
        |       |       |
        8       2       4
        |       |       |
        D --1-- E --7-- F

    MST should have total weight: 4 + 2 + 1 + 4 + 7 = 18
    or equivalently: A-B(4), B-E(2), D-E(1), C-F(4), E-F(7)
    """
    g = AdjacencyMapGraph(directed=False)
    vertices = {}
    for name in "ABCDEF":
        vertices[name] = g.insert_vertex(name)

    g.insert_edge(vertices["A"], vertices["B"], 4)
    g.insert_edge(vertices["B"], vertices["C"], 8)
    g.insert_edge(vertices["A"], vertices["D"], 8)
    g.insert_edge(vertices["B"], vertices["E"], 2)
    g.insert_edge(vertices["C"], vertices["F"], 4)
    g.insert_edge(vertices["D"], vertices["E"], 1)
    g.insert_edge(vertices["E"], vertices["F"], 7)

    return g, vertices


class TestUnionFind:
    """Tests for Union-Find data structure."""

    def test_initial_state(self):
        uf = UnionFind([1, 2, 3, 4, 5])
        # Each element in its own set
        assert uf.find(1) != uf.find(2)
        assert uf.find(2) != uf.find(3)

    def test_union(self):
        uf = UnionFind([1, 2, 3, 4, 5])
        uf.union(1, 2)
        assert uf.find(1) == uf.find(2)
        assert uf.find(1) != uf.find(3)

    def test_union_returns_true_for_different_sets(self):
        uf = UnionFind([1, 2, 3])
        assert uf.union(1, 2) is True

    def test_union_returns_false_for_same_set(self):
        uf = UnionFind([1, 2, 3])
        uf.union(1, 2)
        assert uf.union(1, 2) is False

    def test_transitive_union(self):
        uf = UnionFind([1, 2, 3, 4])
        uf.union(1, 2)
        uf.union(3, 4)
        uf.union(2, 3)
        # All should now be in the same set
        assert uf.find(1) == uf.find(4)


class TestKruskalMST:
    """Tests for Kruskal's algorithm."""

    def test_single_vertex(self):
        g = AdjacencyMapGraph(directed=False)
        g.insert_vertex("A")
        mst = kruskal_mst(g)
        assert len(mst) == 0

    def test_two_vertices(self):
        g = AdjacencyMapGraph(directed=False)
        u = g.insert_vertex("A")
        v = g.insert_vertex("B")
        g.insert_edge(u, v, 5)
        mst = kruskal_mst(g)
        assert len(mst) == 1
        assert mst[0].element() == 5

    def test_sample_graph(self):
        g, vertices = build_weighted_graph()
        mst = kruskal_mst(g)
        assert len(mst) == 5
        total_weight = sum(e.element() for e in mst)
        assert total_weight == 18

    def test_directed_graph_raises(self):
        g = AdjacencyMapGraph(directed=True)
        u = g.insert_vertex("A")
        v = g.insert_vertex("B")
        g.insert_edge(u, v, 5)
        with pytest.raises(ValueError):
            kruskal_mst(g)
