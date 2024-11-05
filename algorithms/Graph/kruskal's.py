from graph_adjacency_list import *

class DisjointSet:
    """A class to represent the disjoint set (Union-Find) with path compression and union by rank."""
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(graph: Graph):
    """
    Kruskal's algorithm to find the minimum spanning tree (MST) of a graph.
    
    :param edges: List of tuples (u, v, weight) representing the edges of the graph.
    :param num_vertices: The number of vertices in the graph.
    :return: List of tuples representing the edges in the MST and the total weight of the MST.
    """
    # number of vertices
    n = len(graph.vertices)

    # get all edges
    edges = []
    for vertex in graph.vertices:
        for edge in vertex.edges:
            edges.append(edge)

    # Sort edges based on their weights
    edges.sort(key=lambda edge: edge.w)
    
    # Create an instance of DisjointSet for tracking connected components
    disjoint_set = DisjointSet(n)
    
    mst = []  # To store the edges in the minimum spanning tree
    total_weight = 0  # To store the total weight of the MST
    
    for edge in edges:
        # Check if adding this edge creates a cycle
        if disjoint_set.find(edge.u) != disjoint_set.find(edge.v):
            disjoint_set.union(edge.u, edge.v)
            mst.append((edge.u, edge.v, edge.w))
            total_weight += edge.w
    
    return mst, total_weight

# # Example usage:
# edges = [
#     (0, 1, 10),
#     (0, 2, 6),
#     (0, 3, 5),
#     (1, 3, 15),
#     (2, 3, 4)
# ]
# num_vertices = 4

# mst, total_weight = kruskal(edges, num_vertices)
# print("Edges in MST:", mst)
# print("Total weight of MST:", total_weight)
    

            

mygraph = Graph(6)
mygraph.add_edge(1,2,10)
mygraph.add_edge(1,3,5)
mygraph.add_edge(2,4,1)
mygraph.add_edge(2,3,3)
mygraph.add_edge(4,5,4)
mygraph.add_edge(4,3,9)
mygraph.add_edge(5,3,2)

print(kruskal(mygraph))

