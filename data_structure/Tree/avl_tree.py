class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

# A utility function to get the 
# height of the tree
def height(node):
    if not node:
        return 0
    return node.height

# A utility function to right rotate 
# subtree rooted with y
def right_rotate(y):
    x = y.left
    T2 = x.right

    # Perform rotation
    x.right = y
    y.left = T2

    # Update heights
    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))

    # Return new root
    return x

# A utility function to left rotate 
# subtree rooted with x
def left_rotate(x):
    y = x.right
    T2 = y.left

    # Perform rotation
    y.left = x
    x.right = T2

    # Update heights
    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))

    # Return new root
    return y

# Get balance factor of node N
def get_balance(node):
    if not node:
        return 0
    return height(node.left) - height(node.right)

# Recursive function to insert a key in
# the subtree rooted with node
def insert(node, key):
  
    # Perform the normal BST insertion
    if not node:
        return Node(key)

    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    else:
        # Equal keys are not allowed in BST
        return node

    # Update height of this ancestor node
    # current node surely has at least one child which is the node we just inserted
    # height() will return 0 if the child is None
    node.height = 1 + max(height(node.left), height(node.right))

    # Get the balance factor of this ancestor node
    balance = get_balance(node)

    # If this node becomes unbalanced, 
    # then there are 4 cases

    # Left Left Case
    # if key < node.left.key, means the node we just inserted is in the left subtree of the current node
    if balance > 1 and key < node.left.key:
        return right_rotate(node)

    # Right Right Case
    if balance < -1 and key > node.right.key:
        return left_rotate(node)

    # Left Right Case
    if balance > 1 and key > node.left.key:
        node.left = left_rotate(node.left)
        return right_rotate(node)

    # Right Left Case
    if balance < -1 and key < node.right.key:
        node.right = right_rotate(node.right)
        return left_rotate(node)

    # Return the (unchanged) node pointer
    return node

def delete(node, key):
    # Basecase 0: if root is None
    if not node:
        return node
    
    # Search for the node to delete
    if key < node.key:
        node.left = delete(node.left, key)
    elif key > node.key:
        node.right = delete(node.right, key)
    else:
        # Found the node to delete
        # Case 1: Node has no children (leaf node)
        if node.left is None and node.right is None:
            return None

        # Case 2: Node has only one child
        elif node.left is None:
            return node.right
        elif node.right is None:
            return node.left

        # Case 3: Node has two children
        else:
            # Find the in-order successor (smallest in the right subtree)
            successor = get_substitute_node(node.right)
            # Copy the successor's key to the current node
            node.key = successor.key
            # Delete the successor
            node.right = delete(node.right, successor.key)
    
    # Step 4: Update height of the current node
    node.height = 1 + max(height(node.left), height(node.right))

    # Step 5: Check balance factor and perform rotations if necessary
    balance = get_balance(node)

    # LL Case
    if balance > 1 and get_balance(node.left) >= 0:
        return right_rotate(node)

    # RR Case
    if balance < -1 and get_balance(node.right) <= 0:
        return left_rotate(node)

    # LR Case
    if balance > 1 and get_balance(node.left) < 0:
        node.left = left_rotate(node.left)
        return right_rotate(node)

    # RL Case
    if balance < -1 and get_balance(node.right) > 0:
        node.right = right_rotate(node.right)
        return left_rotate(node)

    return node

# Helper function to find the minimum value node in a subtree
def get_substitute_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current           


# A utility function to print preorder 
# traversal of the tree
def pre_order(root):
    if root:
        print(root.key, end=" ")
        pre_order(root.left)
        pre_order(root.right)

# Driver code
root = None

# Constructing tree given in the above figure
root = insert(root, 10)
root = insert(root, 20)
root = insert(root, 30)
root = insert(root, 40)
root = insert(root, 50)
root = insert(root, 25)

# The constructed AVL Tree would be
#        30
#       /  \
#      20   40
#     /  \    \
#    10  25   50

print("Preorder traversal :")
pre_order(root)
