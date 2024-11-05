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
        """
        Description:
            To generate a Minimum Spanning Tree (MST) from a graph.
            With slight changes (use MaxHeap; Invert every edge to negative), can generate a Maximum Spanning Tree.

        Time Complexity:
            - O(E logV) using adjacency list
            - O(V^2) using adjacency matrix
        """
        # first reset the distance of each vertex to inf and the previous of each vertex to None 
        self.reset()

        # get the starting vertex
        start_vertex = self.vertices[source]
        # set its distance to 0
        start_vertex.distance = 0

        # # to calculate how many edges we have processed
        num_edges = 0

        total_weight = 0

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
            current_vertex_distance, current_vertex = heapq.heappop(discovered)

            # if it is visited, we pop out another vertex
            # visited means we have already gone thru all its neighbor vertices
            if current_vertex.visited:
                continue

            # if not visited, mark it as visited
            current_vertex.visited = True
            num_edges += 1  # 每次成功加入新的顶点时增加计数
            total_weight += current_vertex_distance

            # # 如果已经添加了 V-1 条边，生成树已经完成，提前终止
            if num_edges == len(self.vertices):
                break

            # go thru all its edges (its neighbor vertex is just edge.v)
            for edge in current_vertex.edges:
                # get the neighbor vertex
                # one edge with one neighbor
                neighbor = edge.v

                # if neighbor's distance is longer, we update its distance and previous
                # it means from the current vertex we can go to its neighbor with a shorter distance
                if neighbor.distance > current_vertex.distance + edge.w:
                    neighbor.distance = edge.w
                    neighbor.previous = current_vertex
                    # push the updated neighbor with new distance to the priority queue
                    heapq.heappush(discovered, (neighbor.distance, neighbor))
                    
        
        return total_weight


    def reset(self):
        for vertex in self.vertices:
            vertex.distance = float('inf')
            vertex.previous = None
            vertex.visited = False

# 测试函数
def test_prim():
    # 创建一个包含5个节点的图
    graph = Graph(9)
    graph.add_edge(0, 1, 4)
    graph.add_edge(1, 7, 11)
    graph.add_edge(1, 2, 8)
    graph.add_edge(2, 3, 7)
    graph.add_edge(2, 8, 2)
    graph.add_edge(2, 5, 4)
    graph.add_edge(3, 4, 9)
    graph.add_edge(3, 5, 14)
    graph.add_edge(4, 5, 10)
    graph.add_edge(5, 6, 2)
    graph.add_edge(6, 7, 1)
    graph.add_edge(6, 8, 6)
    graph.add_edge(7, 8, 7)
    graph.add_edge(7, 0, 8) 

    # 使用 Prim 算法计算最小生成树的总权重
    mst_weight = graph.prim(0)

    # 检查最小生成树的总权重是否正确
    expected_weight = 37
    assert mst_weight == expected_weight, f"Expected weight: {expected_weight}, but got: {mst_weight}"
    print("Test passed! Minimum Spanning Tree weight is correct.")

# 运行测试
test_prim()