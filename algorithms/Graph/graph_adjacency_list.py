from collections import deque
from Edge import Edge
from Vertex import Vertex

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
    
    def dfs(self, start_vertex_id): # O(V+E)
        self.reset()  # 在DFS开始前重置访问状态
        start_vertex = self.vertices[start_vertex_id]

        return self.dfs_recursive(start_vertex)

    def dfs_recursive(self, start_vertex, traversal_result=None): # O(V+E)
        if traversal_result is None:
            traversal_result = []
        
        if not start_vertex.visited:
            start_vertex.visited = True
            traversal_result.append(start_vertex.id)

            for edge in start_vertex.edges:  # 遍历当前顶点的所有边
                neighbor = edge.v if edge.u == start_vertex else edge.u
                if not neighbor.visited:
                    self.dfs_recursive(neighbor, traversal_result)

        return traversal_result

    def bfs_shortest_path(self, start_vertex_id): # O(V+E)
        self.reset()
        start_vertex = self.vertices[start_vertex_id]
        start_vertex.distance = 0
        discovered = deque([start_vertex])
        traversal_result = []

        while discovered:
            current_vertex = discovered.popleft()
            if not current_vertex.visited:
                current_vertex.visited = True
                traversal_result.append([current_vertex.id, current_vertex.distance])

                for edge in current_vertex.edges:
                    neighbor = edge.v if edge.u == current_vertex else edge.u
                    if not neighbor.visited:
                        discovered.append(neighbor)

                    new_distance = current_vertex.distance + 1
                    if new_distance < neighbor.distance:
                        neighbor.distance = new_distance
                        neighbor.predecessor = current_vertex  # 更新前驱顶点

        return traversal_result

    def bfs(self, start_vertex_id): # O(V+E)
        self.reset()

        start_vertex = self.vertices[start_vertex_id]
        discovered = deque([start_vertex]) # to store the vertices we will go thru it's edges later
        traversal_result = [] # to store the final path from start to end

        while discovered:
            current_vertex = discovered.popleft() # each time we pop the leftmost vertex to explore it's edges if it's not visited
            if not current_vertex.visited:
                current_vertex.visited = True
                traversal_result.append(current_vertex.id)

                for edge in current_vertex.edges:
                    neighbor = edge.to_vertex if edge.from_vertex == current_vertex else edge.from_vertex
                    if not neighbor.visited:
                        discovered.append(neighbor)

        return traversal_result

    def kahn_topological_sort(self):
        self.reset()
        start_vertices = deque([v for v in self.vertices if v.in_degree == 0])
        topo_order = []

        while start_vertices:
            current_vertex = start_vertices.popleft()
            topo_order.append(current_vertex.id)

            for edge in current_vertex.edges:
                neighbor = edge.to_vertex
                neighbor.in_degree -= 1
                if neighbor.in_degree == 0:
                    start_vertices.append(neighbor)

        if len(topo_order) == len(self.vertices):
            return topo_order
        else:
            return None  # 图中存在环，无法进行拓扑排序

    def dijkstra(self, start_id):
        """
        find the shortest path from start_id to all other vertices
        only works for non-negative weights graph

        if the graph has negative weights, use bellman-ford algorithm
        """
        self.reset()

        start_vertex = self.vertices[start_id]
        start_vertex.distance = 0       

        priority_queue = MinHeap(len(self.vertices))
        priority_queue.insert((0, start_vertex.id, start_vertex))  # O(logV)

        while not priority_queue.is_empty():
            current_distance, _, current_vertex = priority_queue.extract_min()  # O(logV)

            if current_vertex.visited:
                continue
            current_vertex.visited = True
            
            for edge in current_vertex.edges:
                neighbor = edge.v
                if not neighbor.visited:
                    new_distance = current_distance + edge.w

                    if new_distance < neighbor.distance:
                        neighbor.distance = new_distance
                        neighbor.predecessor = current_vertex  
                        priority_queue.insert((new_distance, neighbor.id, neighbor))  # O(logV)
                else:
                    if neighbor.distance > current_distance + edge.w:
                        priority_queue.update((new_distance, neighbor.id, neighbor)) # O(logV)

    def backtracking(self, target_id: int) -> list: 
        path = []
        if self.vertices[target_id] is None:
            raise ValueError("no path found")

        current_vertex = self.vertices[target_id]

        # Backtrack based on whether it's from the start or the destination
        while current_vertex is not None: # O(L)
            path.append(current_vertex.id)
            current_vertex = current_vertex.predecessor
        
        path.reverse() # O(V)
        return path
    
    def reset(self):
        for vertex in self.vertices:
            vertex.distance = float('inf')
            vertex.previous = None
            vertex.visited = False

    def display_distances(self):
        for vertex in self.vertices:
            print(f"Distance from start to {vertex.id}: {vertex.distance}")


class MinHeap:
    """
    Class description:
    This class implements a MinHeap (also known as a priority queue) which supports insertions, extraction of the minimum element, and updating of elements. 
    The heap is built using a list, and each element in the heap consists of a tuple containing the priority value, vertex ID, and a reference to the vertex object. 
    The position of each vertex in the heap is tracked using a position map, which allows for efficient updates.
    
    Methods:
    - __init__(max_size): Initializes the MinHeap with a maximum size and initializes an empty heap and position map.
    - insert(key): Inserts a new element into the heap.
    - extract_min(): Removes and returns the minimum element from the heap.
    - update(key): Updates the position of an existing element in the heap.
    - rise(index): Maintains heap property by performing a "rise" operation (also called heapify-up).
    - sink(index): Maintains heap property by performing a "sink" operation (also called heapify-down).
    - _swap(i, j): Swaps two elements in the heap and updates their positions in the position map.
    - is_empty(): Checks if the heap is empty.
    """
    def __init__(self, max_size: int) -> None:
        """
        Function description:
        Initializes the MinHeap with the given maximum size. An empty heap and a position map are created.
        
        :Input:
            max_size: The maximum number of elements that can be stored in the heap.
        
        :Output, return or postcondition:
            Initializes the heap and a position map, ready for storing elements.

        :Time complexity:
            O(1)

        :Time complexity analysis:
            The initialization involves setting up an empty list and a position map, both of which are direct allocations that take constant time.

        :Aux space complexity:
            O(n), where n is the maximum size of the heap.

        :Aux space complexity analysis:
            Space is allocated for the heap and the position map, both of which are proportional to the maximum number of elements.
        """
        self.heap = []
        self.position_map = [-1] * max_size  # Initializes position map with -1, this is for update operation
        self.max_size = max_size

    def insert(self, key: tuple) -> None:
        """
        Function description:
        Inserts a new element into the heap and maintains the heap property.
        
        :Input:
            key: A tuple containing (priority, vertex ID, vertex object).
        
        :Output, return or postcondition:
            Inserts the key into the heap while maintaining the heap property.
        
        :Time complexity:
            O(log n), where n is the number of elements in the heap.

        :Time complexity analysis:
            After appending the element to the end of the heap, the `rise` function is called to ensure the heap property is maintained, which operates in logarithmic time.

        :Aux space complexity:
            O(1)

        :Aux space complexity analysis:
            only two temporary variables are used to store the index and vertex ID during the insertion process.
        """
        self.heap.append(key) # O(1)
        index = len(self.heap) - 1
        vertex_id = key[2].id
        self.position_map[vertex_id] = index
        self.rise(index) # O(log n)

    def extract_min(self) -> tuple:
        """
        Function description:
        Removes and returns the minimum element (i.e., the element with the smallest priority) from the heap.
        
        :Input:
            None
        
        :Output, return or postcondition:
            Returns the minimum element from the heap.
        
        :Time complexity:
            O(log n), where n is the number of elements in the heap.

        :Time complexity analysis:
            After removing the root, the last element is moved to the root and the `sink` function is called to restore the heap property, which takes logarithmic time.

        :Aux space complexity:
            O(1)

        :Aux space complexity analysis:
            No additional space is used apart from temporary variables to store elements during the extraction process.
        """
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            min_element = self.heap.pop()
            self.position_map[min_element[2].id] = -1
            return min_element

        root = self.heap[0]
        last_element = self.heap.pop()
        self.heap[0] = last_element
        self.position_map[last_element[2].id] = 0
        self.position_map[root[2].id] = -1
        self.sink(0)
        return root

    def update(self, key: tuple) -> None:
        """
        Function description:
        Updates the position of an element in the heap by reordering it.
        
        :Input:
            key: A tuple containing (priority, vertex ID, vertex object).
        
        :Output, return or postcondition:
            Updates the position of the element in the heap while maintaining the heap property.
        
        :Time complexity:
            O(log n), where n is the number of elements in the heap.

        :Time complexity analysis:
            Both the `rise` and `sink` operations are called to ensure the heap property, each taking logarithmic time.

        :Aux space complexity:
            O(1)

        :Aux space complexity analysis:
            No additional space is used beyond temporary variables to store an index and vertex ID which are integral values.
        """
        vertex_id = key[2].id
        index = self.position_map[vertex_id]
        self.heap[index] = key
        self.rise(index)
        self.sink(index)

    def rise(self, index: int) -> None:
        """
        Function description:
        Moves an element up in the heap until the heap property is restored.
        
        :Input:
            index: The index of the element to move up.
        
        :Output, return or postcondition:
            The element is moved up in the heap to restore the heap property.
        
        :Time complexity:
            O(log n), where n is the number of elements in the heap.

        :Time complexity analysis:
            The `rise` function compares the element with its parent and swaps them if necessary, potentially traversing up to the root of the heap (logarithmic time).

        :Aux space complexity:
            O(1)

        :Aux space complexity analysis:
            No additional space is used beyond temporary variables to store indices.
        """
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index][0] < self.heap[parent_index][0]:
            self._swap(index, parent_index)
            index = parent_index
            parent_index = (index - 1) // 2

    def sink(self, index: int) -> None:
        """
        Function description:
        Moves an element down in the heap until the heap property is restored.
        
        :Input:
            index: The index of the element to move down.
        
        :Output, return or postcondition:
            The element is moved down in the heap to restore the heap property.
        
        :Time complexity:
            O(log n), where n is the number of elements in the heap.

        :Time complexity analysis:
            The `sink` function compares the element with its children and swaps them if necessary, potentially traversing down to the leaves of the heap (logarithmic time).

        :Aux space complexity:
            O(1)

        :Aux space complexity analysis:
            No additional space is used beyond temporary variables to store indices.
        """
        smallest = index
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        if left_child_index < len(self.heap) and self.heap[left_child_index][0] < self.heap[smallest][0]:
            smallest = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index][0] < self.heap[smallest][0]:
            smallest = right_child_index

        if smallest != index:
            self._swap(index, smallest)
            self.sink(smallest)

    def _swap(self, i: int, j: int) -> None:
        """
        Function description:
        Swaps two elements in the heap and updates their positions in the position map.
        
        :Input:
            i: Index of the first element.
            j: Index of the second element.
        
        :Output, return or postcondition:
            Swaps the two elements and updates their positions in the position map.
        
        :Time complexity:
            O(1)

        :Time complexity analysis:
            The swapping operation takes constant time, as it involves a direct exchange of elements in the array.

        :Aux space complexity:
            None

        :Aux space complexity analysis:
            No additional space is used.
        """
        self.position_map[self.heap[i][2].id], self.position_map[self.heap[j][2].id] = j, i
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def is_empty(self) -> bool:
        """
        Function description:
        Checks if the heap is empty.

        :Input:
            None.

        :Output, return or postcondition:
            Returns True if the heap is empty, False otherwise.

        :Time complexity:
            O(1)

        :Time complexity analysis:
            Checking the length of the list is a constant time operation.

        :Aux space complexity:
            None

        :Aux space complexity analysis:
            No additional space is used.
        """
        return len(self.heap) == 0

# 测试代码放在 __name__ == "__main__" 下
if __name__ == "__main__":
    # 创建图
    g = Graph(6)

    # 添加边（有向图和无向图示例）
    g.add_edge(0, 1, 1)
    g.add_edge(0, 2, 2)
    g.add_edge(1, 3, 2)
    g.add_edge(2, 3, 3)
    g.add_edge(3, 4, 4)
    g.add_edge(4, 5, 5)
    # g.add_edge(2, 5, 3)
    # g.add_edge(3, 5, 1)

    # 测试不同的算法
    # print("BFS Shortest Path from A:", g.bfs_shortest_path("A"))
    # print("BFS from A:", g.bfs("A"))
    # print("DFS from A:", g.dfs("A"))
    # print("Kahn's Topological Sort:", g.kahn_topological_sort())
    g.dijkstra(0)
    print("Distances after Dijkstra's algorithm:")
    g.display_distances()
    print("Backtracking path to 5:", g.backtracking(5))
