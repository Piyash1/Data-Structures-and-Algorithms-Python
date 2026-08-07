# 404. Sum of Left Leaves
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumOfLeftLeaves(root: TreeNode) -> int:
    if not root:
        return 0
    
    q = deque([root])
    total = 0
    
    while q:
        node = q.popleft()
        
        # Check if left child exists
        if node.left:
            # If left child is a leaf
            if not node.left.left and not node.left.right:
                total += node.left.val
            else:
                q.append(node.left)
        
        # Push right child if exists
        if node.right:
            q.append(node.right)
    
    return total


if __name__ == "__main__":
    # Example usage:
    # Constructing the binary tree:
    #         3
    #        / \
    #       9  20
    #          / \
    #         15  7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    result = sumOfLeftLeaves(root)
    print(result)  # Output: 24 (9 + 15)
        