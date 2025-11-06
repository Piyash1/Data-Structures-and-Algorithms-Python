"""
        10
       /  \
     20    30
    / \
  40  50
  
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# create nodes
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)


# inorder traversal [Left->Root->Right]
def inorder_traversal(node):
    if node == None:
        return
    inorder_traversal(node.left)
    print(node.data, end=" ")
    inorder_traversal(node.right)

print("\nInorder: ", end=''); inorder_traversal(root)


# preorder traversal [Root->Left->Right]
def preorder_traversal(node):
    if node == None:
        return
    print(node.data, end= " ")
    preorder_traversal(node.left)
    preorder_traversal(node.right)

print("\nPreorder: ", end=" "); preorder_traversal(root)

# postorder traversal [Left->Right->Root]
def postorder_traversal(node):
    if node == None:
        return
    postorder_traversal(node.left)
    postorder_traversal(node.right)
    print(node.data, end=" ")

print("\nPostorder: ", end=" "); postorder_traversal(root); print("\n")

# Level order traversal(BFS)
"""
Example Tree:
        10           <- Level 0 (root)
       /  \
      20   30         <- Level 1
     / \   
    40   50           <- Level 2
    
    Basic Level Order Traversal using Queue
    
    HOW IT WORKS:
    1. Start with root in queue
    2. While queue is not empty:
       - Remove front node from queue
       - Process (print/store) that node
       - Add its left child to queue (if exists)
       - Add its right child to queue (if exists)
    
    Time: O(n), Space: O(w) where w is max width of tree
"""
from collections import deque

def levelorder_traversal(node):
    result = []
    queue = deque([])
    queue.append(node)
    
    while len(queue) != 0:
        e = queue.popleft()
        result.append(e.data) 
        if e.left is not None:
            queue.append(e.left)
        if e.right is not None:
            queue.append(e.right)
    return result

result = levelorder_traversal(root)
print(f"Levelorder: {result}")

    