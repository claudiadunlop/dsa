"""Tests for AdjacencyMapGraph implementation."""

import pytest
from dsa.graphs.adjacency_map import AdjacencyMapGraph


class TestAdjacencyMapGraph:
    """Tests for the AdjacencyMapGraph class."""

    def test_new_graph_is_empty(self):
        g = AdjacencyMapGraph()
        assert g.vertex_count() == 0
        assert g.edge_count() == 0

    def test_insert_vertex(self):
        g = AdjacencyMapGraph()
        v = g.insert_vertex("A")
        assert g.vertex_count() == 1
        assert v.element() == "A"

    def test_insert_edge_undirected(self):
        g = AdjacencyMapGraph(directed=False)
        u = g.insert_vertex("A")
        v = g.insert_vertex("B")
        e = g.insert_edge(u, v, 5)
        assert g.edge_count() == 1
        assert e.element() == 5
        assert g.get_edge(u, v) == e
        assert g.get_edge(v, u) == e

    def test_insert_edge_directed(self):
        g = AdjacencyMapGraph(directed=True)
        u = g.insert_vertex("A")
        v = g.insert_vertex("B")
        e = g.insert_edge(u, v, 5)
        assert g.edge_count() == 1
        assert g.get_edge(u, v) == e
        assert g.get_edge(v, u) is None

    def test_degree_undirected(self):
        g = AdjacencyMapGraph(directed=False)
        u = g.insert_vertex("A")
        v = g.insert_vertex("B")
        w = g.insert_vertex("C")
        g.insert_edge(u, v)
        g.insert_edge(u, w)
        assert g.degree(u) == 2
        assert g.degree(v) == 1
        assert g.degree(w) == 1

    def test_degree_directed(self):
        g = AdjacencyMapGraph(directed=True)
        u = g.insert_vertex("A")
        v = g.insert_vertex("B")
        w = g.insert_vertex("C")
        g.insert_edge(u, v)
        g.insert_edge(u, w)
        g.insert_edge(v, u)
        assert g.degree(u, outgoing=True) == 2
        assert g.degree(u, outgoing=False) == 1

    def test_incident_edges(self):
        g = AdjacencyMapGraph(directed=False)
        u = g.insert_vertex("A")
        v = g.insert_vertex("B")
        w = g.insert_vertex("C")
        e1 = g.insert_edge(u, v)
        e2 = g.insert_edge(u, w)
        edges = set(g.incident_edges(u))
        assert edges == {e1, e2}

    def test_endpoints(self):
        g = AdjacencyMapGraph()
        u = g.insert_vertex("A")
        v = g.insert_vertex("B")
        e = g.insert_edge(u, v)
        endpoints = e.endpoints()
        assert endpoints == (u, v) or endpoints == (v, u)

    def test_opposite(self):
        g = AdjacencyMapGraph()
        u = g.insert_vertex("A")
        v = g.insert_vertex("B")
        e = g.insert_edge(u, v)
        assert e.opposite(u) == v
        assert e.opposite(v) == u

    def test_remove_edge(self):
        g = AdjacencyMapGraph()
        u = g.insert_vertex("A")
        v = g.insert_vertex("B")
        e = g.insert_edge(u, v, 5)
        elem = g.remove_edge(e)
        assert elem == 5
        assert g.edge_count() == 0
        assert g.get_edge(u, v) is None

    def test_remove_vertex(self):
        g = AdjacencyMapGraph()
        u = g.insert_vertex("A")
        v = g.insert_vertex("B")
        w = g.insert_vertex("C")
        g.insert_edge(u, v)
        g.insert_edge(u, w)
        elem = g.remove_vertex(u)
        assert elem == "A"
        assert g.vertex_count() == 2
        assert g.edge_count() == 0

    def test_vertices_iteration(self):
        g = AdjacencyMapGraph()
        v1 = g.insert_vertex("A")
        v2 = g.insert_vertex("B")
        v3 = g.insert_vertex("C")
        vertices = set(g.vertices())
        assert vertices == {v1, v2, v3}

    def test_edges_iteration(self):
        g = AdjacencyMapGraph()
        u = g.insert_vertex("A")
        v = g.insert_vertex("B")
        w = g.insert_vertex("C")
        e1 = g.insert_edge(u, v)
        e2 = g.insert_edge(v, w)
        edges = set(g.edges())
        assert edges == {e1, e2}

    def test_is_directed(self):
        g1 = AdjacencyMapGraph(directed=False)
        g2 = AdjacencyMapGraph(directed=True)
        assert not g1.is_directed()
        assert g2.is_directed()
