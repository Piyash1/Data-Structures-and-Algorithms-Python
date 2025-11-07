# Leetcode no.543 - Diameter of Binary Tree

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    diameter = 0
    
    def diameterOfBinaryTree(self, root):
        self.diameter = 0
        self.height(root)
        return self.diameter
    
    def height(self, node):
        if node is None:
            return 0
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        
        self.diameter = max(self.diameter, left_height+right_height)
        return 1 + max(left_height, right_height)

# Example usage
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    sol = Solution()
    print(sol.diameterOfBinaryTree(root))
    
    
        