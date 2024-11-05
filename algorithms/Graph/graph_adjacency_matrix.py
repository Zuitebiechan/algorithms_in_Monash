import heapq
from collections import deque
from Edge import Edge
from Vertex import Vertex

class Graph:
    def __init__(self, N: int) -> None: 
        # 初始化 N 个顶点
        self.num_vertices = N
        self.vertices = [None] * N  
        for i in range(N):
            self.vertices[i] = Vertex(i)
            
        # 初始化一个 N*N 的邻接矩阵，所有的权重默认为 0（无边）
        self.adj_matrix = [[[float('inf')] for _ in range(N)] for _ in range(N)]

    def add_edge(self, u_id: int, v_id: int, weight: int = 1) -> None:
        # 检查 u_id 和 v_id 是否有效
        if u_id >= self.num_vertices or v_id >= self.num_vertices:
            raise IndexError("Vertex ID out of range.")
        
        # 在邻接矩阵中为边 (u_id, v_id) 设置权重
        self.adj_matrix[u_id][v_id] = weight
    
    def get_edge_weight(self, u_id: int, v_id: int) -> int:
        # 返回指定边的权重
        if u_id >= self.num_vertices or v_id >= self.num_vertices:
            raise IndexError("Vertex ID out of range.")
        
        return self.adj_matrix[u_id][v_id]

    def display_matrix(self) -> None:
        # 显示邻接矩阵
        for row in self.adj_matrix:
            print(row)

    def dfs(self, start_vertex_id):
        self.reset_visits()  # 在DFS开始前重置访问状态
        start_vertex = self.get_vertex(start_vertex_id) # get_vertex() returns a tuple (index, vertex)
        return self.dfs_recursive(start_vertex)

    def dfs_recursive(self, start_vertex, traversal_result=None):
        if traversal_result is None:
            traversal_result = []

        # start_vertex is a tuple (index, vertex), so start_vertex[0] is the index, start_vertex[1] is the vertex object
        start_vertex_idex = start_vertex[0]
        start_vertex_object = start_vertex[1]

        if not start_vertex_object.visited:
            start_vertex_object.visited = True
            traversal_result.append(start_vertex_object.id)

            for i in range(len(self.vertices)):
                if self.adj_matrix[start_vertex_idex][i] != 0:
                    self.dfs_recursive((i, self.vertices[i]), traversal_result)

        return traversal_result

    def bfs_shortest_path(self, start_vertex_id):
        self.reset_visits()

        start_vertex = self.get_vertex(start_vertex_id)[1]  

        start_vertex.distance = 0
        discovered = deque([start_vertex])
        traversal_result = []

        while discovered:
            current_vertex = discovered.popleft()
            current_vertex_index = self.get_vertex(current_vertex.id)[0]

            if not current_vertex.visited:
                current_vertex.visited = True
                traversal_result.append([current_vertex.id, current_vertex.distance])

                for i in range(len(self.vertices)):
                    if self.adj_matrix[current_vertex_index][i] != 0:
                        neighbor = self.vertices[i] 
                        
                        if not neighbor.visited:
                            discovered.append(neighbor)
                            

                        new_distance = current_vertex.distance + 1
                        if new_distance < neighbor.distance:
                            neighbor.distance = new_distance
                            neighbor.previous = current_vertex  # 更新前驱顶点

        return traversal_result

    def bfs(self, start_vertex_id):
        """
        Time Complexity:
            - O(V^2) cuz we need to go thru the entire matrix
        """
        self.reset_visits()

        start_vertex = self.get_vertex(start_vertex_id)[1]  

        discovered = deque([start_vertex])
        traversal_result = []

        while discovered: # O(V) cuz we need to check every vertex
            current_vertex = discovered.popleft()
            current_vertex_index = self.get_vertex(current_vertex.id)[0]

            if not current_vertex.visited:
                current_vertex.visited = True
                traversal_result.append(current_vertex.id)

                for i in range(len(self.vertices)): # O(V) cuz we need to thru the row of this vertex to check how many 1s
                    if self.adj_matrix[current_vertex_index][i] != 0:
                        neighbor = self.vertices[i] 
                        if not neighbor.visited:
                            discovered.append(neighbor)

        return traversal_result

    def kahn_topological_sort(self):
        self.reset_visits()
        
        start_vertices = deque([v for v in self.vertices if v.in_degree == 0])
        topo_order = []

        while start_vertices:
            current_vertex = start_vertices.popleft()
            current_vertex_index = self.get_vertex(current_vertex.id)[0]
            topo_order.append(current_vertex.id)
            
            for i in range(len(self.vertices)):
                if self.adj_matrix[current_vertex_index][i] != 0:
                    neighbor = self.vertices[i]            
                    neighbor.in_degree -= 1

                    if neighbor.in_degree == 0:
                        start_vertices.append(neighbor)

        if len(topo_order) == len(self.vertices):
            return topo_order
        else:
            return None  # 图中存在环，无法进行拓扑排序

    def dijkstra(self, start_id):
        """
        Time Complexity:
            - O(V^2) cuz we need to go thru the entire matrix
        
        """
        self.reset_visits() # O(V)
        self.reset_distances() # O(V)

        start_vertex = self.get_vertex(start_id)[1]

        start_vertex.distance = 0       

        priority_queue = []
        # 使用顶点的距离和它的值（字符串）作为排序的依据
        heapq.heappush(priority_queue, (0, start_vertex.id, start_vertex))

        while priority_queue: # O(V) cuz we need to check every vertex
            current_distance, _, current_vertex = heapq.heappop(priority_queue)

            current_vertex_index = self.get_vertex(current_vertex.id)[0]

            if current_vertex.visited:
                continue

            current_vertex.visited = True

            for i in range(len(self.vertices)):# O(V^2) 
                if self.adj_matrix[current_vertex_index][i] != 0:
                    neighbor = self.vertices[i] 
                    new_distance = current_distance + self.adj_matrix[current_vertex_index][i]

                    if new_distance < neighbor.distance:
                        neighbor.distance = new_distance
                        neighbor.previous = current_vertex
                        heapq.heappush(priority_queue, (new_distance, neighbor.id, neighbor))

    def backtracking(self, target_id):
        path = []
        current_vertex = self.get_vertex(target_id)[1]

        while current_vertex is not None:
            path.append(current_vertex.id)
            current_vertex = current_vertex.previous

        path.reverse()  # 逆序排列，从源顶点到目标顶点
        return path

    def reset_visits(self):
        for vertex in self.vertices:
            vertex.visited = False
    
    def reset_distances(self):
        for vertex in self.vertices:
            vertex.distance = float('inf')
            vertex.previous = None
    
    def get_vertex(self, vertex_id):
        for index, vertex in enumerate(self.vertices):
            if vertex.id == vertex_id:
                return (index, vertex)
        raise ValueError(f"Vertex with id {vertex_id} not found")

    def display_distances(self):
        for vertex in self.vertices:
            print(f"Distance from start to {vertex.id}: {vertex.distance}")



# 测试代码放在 __name__ == "__main__" 下
if __name__ == "__main__":
    # 创建图
    g = Graph()

    # 添加顶点
    g.add_vertex('A')
    g.add_vertex('B')
    g.add_vertex('C')
    g.add_vertex('D')
    g.add_vertex('E')

    # 添加边 (有向图)
    g.add_edge('A', 'B', 2)
    g.add_edge('A', 'C', 1)
    g.add_edge('B', 'D', 3)
    g.add_edge('C', 'D', 4)
    g.add_edge('D', 'E', 5)
    g.add_edge('C', 'E', 8)

    # 测试 DFS
    print("\nDFS starting from vertex A:")
    dfs_result = g.dfs('A')
    print("DFS traversal order:", dfs_result)

    # 测试 BFS
    print("\nBFS starting from vertex A:")
    bfs_result = g.bfs('A')
    print("BFS traversal order:", bfs_result)

    # 测试 BFS Shortest Path
    print("\nBFS Shortest Path from vertex A:")
    bfs_shortest_result = g.bfs_shortest_path('A')
    print("BFS Shortest Path (vertex, distance):", bfs_shortest_result)

    # 测试 Kahn's Topological Sort
    print("\nKahn's Topological Sort:")
    topo_sort_result = g.kahn_topological_sort()
    print("Topological Sort order:", topo_sort_result)

    # 测试 Dijkstra's Algorithm
    print("\nDijkstra's Shortest Path from vertex A:")
    g.dijkstra('A')
    g.display_distances()

    # 测试 Backtracking
    print("\nBacktracking path from E to A:")
    backtrack_result = g.backtracking('E')
    print("Backtracked path:", backtrack_result)