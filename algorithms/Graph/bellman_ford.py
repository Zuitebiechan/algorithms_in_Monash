from Edge import Edge
from Vertex import Vertex
from typing import List


def BellmanFord(vertices: List[Vertex], edges: List[Edge], source: Vertex):
    """
    Bellman-Ford algorithm for finding the shortest path from a source vertex to all other vertices in a graph with negative edge.
    :param vertices: List of vertices in the graph
    :param edges: List of edges in the graph
    :param source: Source vertex
    :return: None

    Time Complexity:
        - O(V*E) using adjacency list
        - O(V^2 + VE) using adjacency matrix cuz we need to go thru the entire matrix(V^2) V times
        - Actually we need to consider how to get the edges: List[Edge].
            - For adjacency list, go thru each vertex's edges -> O(V+E + O(BellmanFord)) = O(V*E)
            - For adjacency matrix, go thru the entire matrix -> O(V^2 + O(BellmanFord)) = O(V^2 + VE)
        
        - note
            - For sparse graph, E = V or E = V logV -> O(V^2) or O(V^2 logV) 
            - For dense graph, E = V^2 -> O(V^3)

    Aux Space Complexity:
        - O(V) cuz each vertex needs to store its distance and previous
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
    for i in range(len(vertices) - 1):
        updated = False  # Track if any update happens in this round

        for edge in edges:
            if edge.u.distance + edge.w < edge.v.distance:
                edge.v.distance = edge.u.distance + edge.w
                edge.v.previous = edge.u
                updated = True

        # If no update happened in this round, we can terminate early
        if not updated:
            print(f"Terminated early after {i + 1} iterations")
            break

    # Check for negative-weight cycles
    # Complexity: O(E)
    for edge in edges:
        if edge.u.distance + edge.w < edge.v.distance:
            raise ValueError("Graph contains a negative-weight cycle")


