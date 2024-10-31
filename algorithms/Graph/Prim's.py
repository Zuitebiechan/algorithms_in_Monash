from collections import deque
from Edge import Edge
from Vertex import Vertex
import heapq

class Graph:
    def __init__(self, N: int) -> None: 
        self.vertices = [None] * N  
        for i in range(N):
            self.vertices[i] = Vertex(i) 

    def add_edge(self, u_id: int, v_id: int, w: int) -> None:
        u = self.vertices[u_id]
        v = self.vertices[v_id]
        
        edge = Edge(u, v, w)
        u.add_edge(edge)

    def prim(self, source: int):
        # first reset the distance of each vertex to inf and the previous of each vertex to None 
        self.reset()

        # get the starting vertex
        start_vertex = self.vertices[source]
        # set its distance to 0
        start_vertex.distance = 0

        ## add starting vertex to the discovered list
        # each time we will pop out one vertex from the list and mark it as visited
        # and add all its neighbor vertices to the list 
        # repeat this until the list is empty
        # Priority queue to select the minimum edge weight vertex each time
        # Format of each entry: (distance, vertex)
        discovered = []
        heapq.heappush(discovered, (0, start_vertex))

        # starting repeat
        while discovered:
            # pop out one vertex
            current_vertex = heapq.heappop()

            # if it is visited, we pop out another vertex
            # visited means we have already gone thru all its neighbor vertices
            if current_vertex.visited:
                continue

            # if not visited, mark it as visited
            current_vertex.visited = True

            # go thru all its edges (its neighbor vertex is just edge.v)
            for edge in current_vertex.edges:
                # get the neighbor vertex
                # one edge with one neighbor
                neighbor = edge.v

                # if neighbor's distance is longer, we update its distance and previous
                # it means from the current vertex we can go to its neighbor with a shorter distance
                if neighbor.distance < current_vertex.distance + edge.w:
                    neighbor.distance = edge.w
                    neighbor.previous = current_vertex
                    # push the updated neighbor with new distance to the priority queue
                    heapq.heappush(discovered, (neighbor.distance, neighbor))
            




    def reset(self):
        for vertex in self.vertices:
            vertex.distance = float('inf')
            vertex.previous = None
            vertex.visited = False