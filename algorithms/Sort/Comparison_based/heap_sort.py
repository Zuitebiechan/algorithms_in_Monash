class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, key):
        """Insert a new key into the heap."""
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        """Remove and return the minimum element from the heap."""
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        # Move the last element to the root and heapify down
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def get_min(self):
        """Return the minimum element from the heap without removing it."""
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def _heapify_up(self, index):
        """Heapify up to maintain the heap property after insertion."""
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        """Heapify down to maintain the heap property after extracting the min element."""
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest = index

        if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
            smallest = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
            smallest = right_child_index

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def __len__(self):
        """Return the number of elements in the heap."""
        return len(self.heap)

    def is_empty(self):
        
        """Check if the heap is empty."""
        return len(self.heapa) == 0