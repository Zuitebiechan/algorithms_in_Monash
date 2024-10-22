from abstract_queue import Queue
from array import ArrayR
from typing import TypeVar, Generic
T = TypeVar('T')


class LinearQueue(Queue[T]):
    """
    add item at position rear, serve item at position front
    Two pointers: front and rear
    positions before front cannot be used once front move forward -> a waste of spaces, many empty cells

    Invariants:
        - (rear - front) = len(array) (no. of items in the queue)
        - items are always stored from front to rear-1 (front is the first item and rear-1 is the last one)
    """
    def __init__(self, max_capacity: int) -> None:
        super().__init__()
        self.front = 0
        self.rear = 0
        self.array = ArrayR(max_capacity)
    
    def append(self, item: T) -> None:
        """
        will add an item at the end of the queue
        """
        if self.is_full(self):
            raise Exception("Queue is full")
        
        self.array[self.rear] = item
        self.rear += 1
        self.length += 1

    def serve(self) -> T:
        """
        will get the first item in the queue and delete it
        """
        if self.is_full(self):
            raise Exception("Queue is full")
        
        self.length -= 1
        item = self.array[self.front]
        self.front += 1
        return item

    def clear(self):
        super.__init__(self)
        self.front = 0
        self.rear = 0

    def is_full(self) -> bool:
        return self.rear == len(self.array)

