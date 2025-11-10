# Leetcode no.98 - Validate Binary Search Tree

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def isValidBST(self, root):
        
        def isValid(node, left, right):
            if not node:
                return True
            if not (node.val > left and node.val < right):
                return False
            
            return (isValid(node.left, left, node.val) and isValid(node.right, node.val, right))
        return isValid(root, float("-inf"), float("inf"))

# Example usage
if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    solution = Solution()
    print(solution.isValidBST(root))