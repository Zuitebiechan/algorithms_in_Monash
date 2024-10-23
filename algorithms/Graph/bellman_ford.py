from Edge import Edge
from Vertex import Vertex
from typing import List


def BellmanFord(vertices: List[Vertex], edges: List[Edge], source: Vertex):
    """
    Bellman-Ford algorithm for finding the shortest path from a source vertex to all other vertices in a graph.
    :param vertices: List of vertices in the graph
    :param edges: List of edges in the graph
    :param source: Source vertex
    :return: None

    Complexity:
    - Time: O(V*E)
    """
    # Initialize the distance of the source vertex to 0 and all other vertices to infinity
    # Complexity: O(V)
    for v in vertices:
        if v == source:
            v.distance = 0
        else:
            v.distance = float('inf')
        v.previous = None

    # Relax all edges V-1 times
    # Complexity: O(V*E)
    for _ in range(len(vertices) - 1):
        for edge in edges:
            if edge.u.distance + edge.w < edge.v.distance:
                edge.v.distance = edge.u.distance + edge.w
                edge.v.previous = edge.u

    # Check for negative-weight cycles
    # Complexity: O(E)
    for edge in edges:
        if edge.u.distance + edge.w < edge.v.distance:
            raise ValueError("Graph contains a negative-weight cycle")


