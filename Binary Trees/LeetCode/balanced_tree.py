# Leetcode no.110 - Balanced Binary Tree

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def isBalanced(self, root):
        height_diff = self.checkHeight(root)
        if height_diff == -1:
            return False
        return True
    
    def checkHeight(self, node):
        if node is None:
            return 0
        
        left_height = self.checkHeight(node.left)
        if left_height == -1:
            return -1
        right_height = self.checkHeight(node.right)
        if right_height == -1:
            return -1
        
        if abs(left_height-right_height) > 1:
            return -1
        
        return 1 + max(left_height, right_height)
        
# Example usage
if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    sol = Solution()
    print(sol.isBalanced(root))