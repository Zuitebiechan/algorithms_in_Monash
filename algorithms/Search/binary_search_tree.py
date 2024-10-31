from typing import Callable, TypeVar, Generic
from data_structure.Stack.stack import Stack

K = TypeVar('K')
I = TypeVar('I')


class BinarySearchTreeNode(Generic[K, I]):
    def __init__(self, key: K, item: I = None) -> None:
        self.key = key
        self.item = item
        self.left = None # left node
        self.right = None # right node

    def __str__(self) -> str:
        return " (" + str(self.key) + ", " + str(self.item) + ")"
    
class BinarySearchTree(Generic[K, I]):
    def __init__(self) -> None:
        self.root = None

    def __contains__(self, key: K) -> bool: # check if an item is in the tree
        return self.find_aux(self.root, key)
    
    def find_aux(self, current: BinarySearchTreeNode[K, I], key) -> bool:
        if current is None: # basecase: empty
            return False
        
        elif key == current.key: # basecase: found
            return True
        
        elif key < current.key:
            return self.find_aux(current.left, key)
        
        elif key > current.key:
            return self.find_aux(current.right, key)
    
    def __getitem__(self, key: K) -> I:
        return self.getitem_aux(self.root, key)
    
    def getitem_aux(self, current: BinarySearchTreeNode[K, I], key) -> I:
        if current is None: # basecase: empty
            raise KeyError("Key not found")
        
        elif key == current.key: # basecase: found
            return current.item
        
        elif key < current.key:
            return self.getitem_aux(current.left, key)

        elif key > current.key:
            return self.getitem_aux(current.right, key)
    
    def __setitem__(self, key: K, item: I) -> None:
        self.insert_aux(self.root, key, item)
    
    def insert_aux(self, current: BinarySearchTreeNode[K, I], key: K, item: I) -> BinarySearchTreeNode[K, I]:
        if current is None: # basecase: insert at leaf node
            current = BinarySearchTreeNode(key, item)
        
        elif key == current.key: # basecase: duplicate then change 
            current.item = item
        
        elif key < current.key:
            current.left = self.insert_aux(current.left, key, item)

        elif key > current.key:
            current.right = self.insert_aux(current.right, key, item)
        
        return current
    
    def get_leaves(self) -> list:
        leaves_list = []
        self.get_leaves_aux(self, self.root, leaves_list)
        return leaves_list
    
    def get_leaves_aux(self, current: BinarySearchTreeNode[K, I], leaves_list) -> None:
        # base case1: empty node -> does nothing
        if current is not None:
            if self.is_leaf(current):
                leaves_list.append(current.item)
            else:
                self.get_leaves_aux(current.left, leaves_list)
                self.get_leaves_aux(current.right, leaves_list)

    def is_leaf(self, node: BinarySearchTreeNode[K, I]) -> bool:
        return node.left is None and node.right is None

    def delete(self, key: K) -> None:
        pass
        
    def __iter__(self):
        return PreOrderIteratorBST(self.root)
    
    def is_empty(self) -> bool:
        return self.root is None


class PreOrderIteratorBST:
    def __init__(self, root: BinarySearchTreeNode[K, I]) -> None:
        self.stack = Stack()
        self.stack.push(root)

    def __iter__(self):
        return self
    
    def __next__(self) -> I:
        if self.stack.is_empty():
            raise StopIteration
        
        current = self.stack.pop()
        if current.right is not None:
            self.stack.push(current.right)
        if current.left is not None:
            self.stack.push(current.right)

        return current.item