# Given the root of a Binary Search Tree. Your task is to find the minimum element in this given BST.

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def minValue(self, root):
        if not root:
            return None
        while root and root.left:
            root = root.left
        return root.data
    
    def maxValue(self, root):
        if not root:
            return None
        while root and root.right:
            root = root.right
        return root.data

if __name__ == "__main__":
    root = Node(4)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(1)
    root.left.right = Node(3)
    
    sol = Solution()
    min = sol.minValue(root)
    max = sol.maxValue(root)
    print(f"Minimum element in BST: {min}")
    print(f"Max element in BST: {max}")