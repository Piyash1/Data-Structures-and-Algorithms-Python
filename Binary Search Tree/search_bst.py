# Leetcode no.700 - Search in a Binary Search Tree

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def searchBST(self, root, val):
        if not root:
            return None
        while root:
            if root.val == val:
                return root
            if val < root.val:
                root = root.left
            else:
                root = root.right
        return root

# Example usage
if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    
    sol = Solution()
    val = 2
    result = sol.searchBST(root, val)
    if result:
        print(result.val)
    else:
        print("Not found")