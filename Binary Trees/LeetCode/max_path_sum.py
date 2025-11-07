# Leetcode no.124 - Binary Tree Maximum Path Sum

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    maximum = float("-inf")
    
    def maxPathSum(self, root):
        self.findMax(root)
        return self.maximum
    
    def findMax(self, node):
        if node is None:
            return 0
        left_path_sum = self.findMax(node.left)
        right_path_sum = self.findMax(node.right)
        
        if left_path_sum < 0:
            left_path_sum = 0
        if right_path_sum < 0:
            right_path_sum = 0
        
        self.maximum = max(self.maximum, left_path_sum+ node.val + right_path_sum)
        return max(left_path_sum, right_path_sum) + node.val

# Example usage
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    
    sol = Solution()
    print(sol.maxPathSum(root))