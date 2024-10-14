class Node:
    """
    A class representing a single node in a binary tree.

    Attributes:
    -----------
    value : int
        The value of the node.
    left : Node
        The left child of the node.
    right : Node
        The right child of the node.
    """

    def __init__(self, value):
        """
        Initialize the node with a value, and set left and right children to None.

        Parameters:
        -----------
        value : int
            The value of the node.
        """
        self.value = value  # Node value
        self.left = None    # Left child
        self.right = None   # Right child

class BinaryTree:
    """
    A class representing a binary tree.

    Methods:
    --------
    insert(value)
        Inserts a new value into the binary tree.
    in_order_traversal(node)
        Performs in-order traversal (left, root, right) of the binary tree.
    pre_order_traversal(node)
        Performs pre-order traversal (root, left, right) of the binary tree.
    post_order_traversal(node)
        Performs post-order traversal (left, right, root) of the binary tree.
    """

    def __init__(self):
        """
        Initialize the binary tree with no root node.
        """
        self.root = None  # Root of the binary tree is initially None

    def insert(self, value):
        """
        Insert a new node with the given value into the binary tree.
        
        Parameters:
        -----------
        value : int
            The value to be inserted into the binary tree.

        Time Complexity:
        ---------------
        Best Case: O(1) - Inserting into an empty tree
        Average Case: O(log N) - Inserting into a balanced tree
        Worst Case: O(N) - Inserting into a skewed tree where N is the number of nodes in the tree
        """
        if self.root is None:
            # If the tree is empty, set the root to be the new node
            self.root = Node(value)
        else:
            # Otherwise, insert recursively starting from the root
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        """
        A helper function to insert a new node into the tree recursively.

        Parameters:
        -----------
        current_node : Node
            The current node in the recursive traversal.
        value : int
            The value to be inserted.
        """
        if value < current_node.value:
            # Go to the left subtree if the new value is less than the current node's value
            if current_node.left is None:
                current_node.left = Node(value)  # Insert here if left child is empty
            else:
                self._insert_recursive(current_node.left, value)  # Recur on the left child
        else:
            # Go to the right subtree if the new value is greater or equal
            if current_node.right is None:
                current_node.right = Node(value)  # Insert here if right child is empty
            else:
                self._insert_recursive(current_node.right, value)  # Recur on the right child

    def in_order_traversal(self, node):
        """
        Perform an in-order traversal of the binary tree.
        Visit left subtree, current node, then right subtree.

        Example:
        --------
        Given a binary tree:
            10
           /  \
          5   20
         / \    \
        3   7    25

        The in-order traversal should return [3, 5, 7, 10, 20, 25].

        Parameters:
        -----------
        node : Node
            The starting node for the traversal (usually the root).

        Returns:
        --------
        List[int]
            A list of values visited in in-order.
        """
        values = []
        if node:
            values += self.in_order_traversal(node.left)  # Visit left subtree
            values.append(node.value)                    # Visit current node
            values += self.in_order_traversal(node.right) # Visit right subtree
        return values

    def pre_order_traversal(self, node):
        """
        Perform a pre-order traversal of the binary tree.
        Visit current node, left subtree, then right subtree.

        Example:
        --------
        Given a binary tree:
            10
           /  \
          5   20
         / \    \
        3   7    25

        The pre-order traversal should return [10, 5, 3, 7, 20, 25].

        Parameters:
        -----------
        node : Node
            The starting node for the traversal (usually the root).

        Returns:
        --------
        List[int]
            A list of values visited in pre-order.
        """
        values = []
        if node:
            values.append(node.value)                     # Visit current node
            values += self.pre_order_traversal(node.left)  # Visit left subtree
            values += self.pre_order_traversal(node.right) # Visit right subtree
        return values

    def post_order_traversal(self, node):
        """
        Perform a post-order traversal of the binary tree.
        Visit left subtree, right subtree, then current node.

        Example:
        --------
        Given a binary tree:
            10
           /  \
          5   20
         / \    \
        3   7    25

        The post-order traversal should return [3, 7, 5, 25, 20, 10].

        Parameters:
        -----------
        node : Node
            The starting node for the traversal (usually the root).

        Returns:
        --------
        List[int]
            A list of values visited in post-order.
        """
        values = []
        if node:
            values += self.post_order_traversal(node.left)  # Visit left subtree
            values += self.post_order_traversal(node.right) # Visit right subtree
            values.append(node.value)                       # Visit current node
        return values

# Example usage:
if __name__ == "__main__":
    tree = BinaryTree()

    # Insert elements into the binary tree
    tree.insert(10)
    tree.insert(5)
    tree.insert(20)
    tree.insert(3)
    tree.insert(7)
    tree.insert(15)
    tree.insert(25)

    # In-order traversal (should print: [3, 5, 7, 10, 15, 20, 25])
    print("In-order Traversal:", tree.in_order_traversal(tree.root))

    # Pre-order traversal (should print: [10, 5, 3, 7, 20, 15, 25])
    print("Pre-order Traversal:", tree.pre_order_traversal(tree.root))

    # Post-order traversal (should print: [3, 7, 5, 15, 25, 20, 10])
    print("Post-order Traversal:", tree.post_order_traversal(tree.root))