# You are given the root of a BST and an integer key. You need to find the inorder predecessor and successor of the given key. If either predecessor or successor is not found, then set it to NULL.


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def findPreSuc(self, root, key):
        predecessor = self.findPredecessor(root, key)
        successor = self.findSuccessor(root, key)
        return predecessor, successor
    
    def findPredecessor(self, root, key):
        predecessor = None
        current = root
        
        while current:
            if current.data < key:
                predecessor = current
                current = current.right
            else:
                current = current.left
        return predecessor
    
    def findSuccessor(self, root, key):
        successor = None
        current = root
        
        while current:
            if current.data > key:
                successor = current
                current = current.left
            else:
                current = current.right
        return successor

# Example Usage
if __name__ == "__main__":
    # Build tree:
    #       50
    #      /  \
    #    30    70
    #   / \    / \
    #  20 40  60 80
    
    root = TreeNode(50)
    root.left = TreeNode(30)
    root.right = TreeNode(70)
    root.left.left = TreeNode(20)
    root.left.right = TreeNode(40)
    root.right.left = TreeNode(60)
    root.right.right = TreeNode(80)
    
    sol = Solution()
    
    # Inorder: [20, 30, 40, 50, 60, 70, 80]
    
    # Test case 1: Key = 50
    pred, succ = sol.findPreSuc(root, 50)
    print(f"Key: 50")
    print(f"Predecessor: {pred.data if pred else None}")  # 40
    print(f"Successor: {succ.data if succ else None}")    # 60
    print()