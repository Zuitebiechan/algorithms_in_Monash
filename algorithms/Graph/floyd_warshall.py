class Graph:
    """
    matrix: 2D list, tuple (distance, middleman)
    Example:
        0    1    2    3
    0   0    4    2    inf
    1   4    0    3    inf
    2   2    inf  0    2
    3   inf  inf  2    0

    From self to self, the distance is 0, and the middleman is None
    Infinity means unreachable
    if there's a negative cycle, self.dist_matrix[i][i] will be negative
    """
    def __init__(self, N: int) -> None: 
        self.num_vertices = N
        # initialize dist_matrix, tuple (distance, middleman)
        self.dist_matrix = [[(float('inf'), None)] * N for _ in range(N)]
        
        # initialize the distance from self to self as 0, and the middleman as None
        for i in range(N):
            self.dist_matrix[i][i] = (0, None)

    def add_edge(self, u_id: int, v_id: int, weight: int) -> None:
        self.dist_matrix[u_id][v_id] = (weight, None)

    def floyd_warshall(self):
        """
        Time complexity:
            O(V^3) where V is the no. of vertices in the graph
        
        """
        for k in range(self.num_vertices):
            for i in range(self.num_vertices):
                for j in range(self.num_vertices):
                    # if i to k to j is shorter than i to j directly
                    if self.dist_matrix[i][j][0] > self.dist_matrix[i][k][0] + self.dist_matrix[k][j][0]:
                        # update the distance and middleman
                        self.dist_matrix[i][j] = (self.dist_matrix[i][k][0] + self.dist_matrix[k][j][0], k)

    def get_path(self, i, j, path=None):
        # initialize the path list
        if path is None:
            path = []
        
        # if the distance is infinity, it means i to j is unreachable, return empty list
        if self.dist_matrix[i][j][0] == float('inf'):
            raise ValueError(f"{i} and {j} are unreachable")
        
        # if i and j are the same, return the node i
        if i == j:
            path.append(i)
            return path

        # get the middleman of the path from i to j
        middleman = self.dist_matrix[i][j][1]
        if middleman is None:
            # if the path is empty or the last node is not i, add i to the path
            if not path or path[-1] != i:
                path.append(i)
            path.append(j)
            return path

        # recursively get the path from i to middleman and from middleman to j
        self.get_path(i, middleman, path)
        self.get_path(middleman, j, path)

        return path
    
    def display_matrix(self) -> None:
        for row in self.dist_matrix:
            print(row)




# More complex test case
def complex_test_case():
    print("Starting complex test case:")
    g = Graph(6)
    
    # Add edges
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 2)
    g.add_edge(1, 2, 1)
    g.add_edge(1, 3, 5)
    g.add_edge(2, 3, 8)
    g.add_edge(2, 4, 10)
    g.add_edge(3, 4, 2)
    g.add_edge(3, 5, 6)
    g.add_edge(4, 5, 3)
    
    print("Initial distance matrix:")
    g.display_matrix()
    
    # Run Floyd-Warshall algorithm
    g.floyd_warshall()
    
    print("\nDistance matrix after running Floyd-Warshall algorithm:")
    g.display_matrix()
    
    # Test various paths
    test_paths = [(0, 5), (1, 4), (2, 5), (0, 3)]
    for start, end in test_paths:
        try:
            path = g.get_path(start, end)
            distance = g.dist_matrix[start][end][0]
            print(f"\nShortest path from {start} to {end}: {path}")
            print(f"Distance: {distance}")
        except ValueError as e:
            print(f"\nError: {e}")
    
    # Test unreachable case
    g.add_edge(5, 0, float('inf'))
    try:
        path = g.get_path(5, 0)
    except ValueError as e:
        print(f"\nExpected error: {e}")
    
    # Test negative cycle
    g_negative = Graph(3)
    g_negative.add_edge(0, 1, 1)
    g_negative.add_edge(1, 2, -3)
    g_negative.add_edge(2, 0, 1)
    g_negative.floyd_warshall()
    print("\nDistance matrix of graph with negative cycle:")
    g_negative.display_matrix()

# Run complex test case
complex_test_case()