"""Shortest path algorithms."""

from dsa.graphs.base import Graph
from typing import TypeVar, Dict, Tuple, Optional
from dsa.priority_queues import heap

V = TypeVar('V')
E = TypeVar('E')


def dijkstra(graph: Graph[V, E], start: Graph.Vertex) -> Tuple[
        Dict[Graph.Vertex, float], Dict[Graph.Vertex, Graph.Edge]]:
    """Compute shortest paths from start using Dijkstra's algorithm.

    Dijkstra's algorithm finds shortest paths from a source vertex to all
    other vertices in a weighted graph with non-negative edge weights.

    Assumes edge elements are numeric weights.

    Args:
        graph: A graph with non-negative edge weights.
        start: The source vertex.

    Returns:
        A tuple (distances, predecessors) where:
        - distances: Dict mapping each reachable vertex to its distance from start
        - predecessors: Dict mapping each reachable vertex (except start) to the
                        edge on its shortest path

    Raises:
        ValueError: If any edge weight is negative.
    """
    d = {v: float('inf') for v in graph.vertices()}
    d[start] = 0

    pred: Dict[Graph.Vertex, Graph.Edge] = {}

    pq = heap.Heap()
    pq.add(0, start)

    while not pq.is_empty():
        key, u = pq.remove_min()

        if key > d[u]:
            continue

        for e in graph.incident_edges(u):
            v = e.opposite(u)
            weight = e.element()   # <-- THIS is correct for your Graph

            if weight < 0:
                raise ValueError("Graph has negative edge weight")

            if d[u] + weight < d[v]:
                d[v] = d[u] + weight
                pred[v] = e
                pq.add(d[v], v)

    return d, pred
    #raise NotImplementedError


def shortest_path(graph: Graph[V, E], start: Graph.Vertex,
                  end: Graph.Vertex) -> Tuple[float, list]:
    """Find the shortest path from start to end.

    Args:
        graph: A graph with non-negative edge weights.
        start: The source vertex.
        end: The destination vertex.

    Returns:
        A tuple (distance, path) where:
        - distance: The total distance from start to end (float('inf') if unreachable)
        - path: List of vertices from start to end (empty if unreachable)
    """
    d, pred = dijkstra(graph, start)

    if end not in d or d[end] == float('inf'):
        return float('inf'), []

    path = []
    current = end

    while current != start:
        path.append(current)
        e = pred[current]
        current = e.opposite(current)

    path.append(start)
    path.reverse()

    return d[end], path
    #raise NotImplementedError


def bellman_ford(graph: Graph[V, E], start: Graph.Vertex) -> Tuple[
        Dict[Graph.Vertex, float], Dict[Graph.Vertex, Graph.Edge]]:
    """Compute shortest paths from start using Bellman-Ford algorithm.

    Bellman-Ford handles graphs with negative edge weights and can detect
    negative cycles. It runs in O(VE) time.

    Assumes edge elements are numeric weights.

    Args:
        graph: A directed graph (may have negative edge weights).
        start: The source vertex.

    Returns:
        A tuple (distances, predecessors) where:
        - distances: Dict mapping each reachable vertex to its distance from start
        - predecessors: Dict mapping each reachable vertex (except start) to the
                        edge on its shortest path

    Raises:
        ValueError: If a negative cycle is reachable from start.
    """
    d = {v: float('inf') for v in graph.vertices()}
    d[start] = 0

    pred: Dict[Graph.Vertex, Graph.Edge] = {}

    vertices = list(graph.vertices())

    for _ in range(len(vertices) - 1):
        for u in vertices:
            for e in graph.incident_edges(u):
                v = e.opposite(u)
                weight = e.element()

                if d[u] + weight < d[v]:
                    d[v] = d[u] + weight
                    pred[v] = e

    for u in vertices:
        for e in graph.incident_edges(u):
            v = e.opposite(u)
            weight = e.element()

            if d[u] + weight < d[v]:
                raise ValueError("Graph contains a negative cycle")

    return d, pred
    #raise NotImplementedError

