def warshalls(graph):
    """
    Time complexity: 
        - O(V^3) where V is the number of vertices in the graph
    """
    n = len(graph.vertices)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph.adjacency_matrix[i][k] and graph.adjacency_matrix[k][j] or graph.adjacency_matrix[i][j]:
                    graph.adjacency_matrix[i][j] = True
