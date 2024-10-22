from abstract_queue import Queue
from array import ArrayR
from typing import TypeVar, Generic
T = TypeVar('T')


class CircularQueue(Queue[T]):
    """
    Two pointers: front and rear
    front and rear can go back to the head of queue when reach the end of it -> space efficient

    Invariants:
        - If front <= rear: from front to rear-1, in that order
        - Else: from front to the end of the array and from 0 to rear-1, in that order
    """
    def __init__(self, max_capacity: int) -> None:
        MIN_CAPACITY = 1
        super().__init__()
        self.front = 0
        self.rear = 0
        self.array = ArrayR(max(self.MIN_CAPACITY, max_capacity))
    
    def append(self, item: T) -> None:
        """
        will add an item at the end of the queue
        """
        if self.is_full(self):
            raise Exception("Queue is full")
        
        self.array[self.rear] = item
        self.rear = (self.rear + 1) % len(self.array) # make sure rear always move between 0 to len(self,array)-1
        self.length += 1

    def serve(self) -> T:
        """
        will get the first item in the queue and delete it
        """
        if self.is_full(self):
            raise Exception("Queue is full")
        
        self.length -= 1
        item = self.array[self.front]
        self.front = (self.front+1) % len(self.array) # make sure front always move between 0 to len(self,array)-1
        return item

    def clear(self):
        super.__init__(self)
        self.front = 0
        self.rear = 0

    def is_full(self) -> bool:
        return len(self) == len(self.array)
    
    def print_items(self) -> None:
        index = self.front

        for _ in range(len(self)):
            print(self.array[index])
            index = (index + 1) % len(self.array)
