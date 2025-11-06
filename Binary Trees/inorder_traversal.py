# Leetcode no.94 - Binary Tree Inorder Traversal

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def inorderTraversal(self, root):
        result = []
        
        def dfs(node):
            if node == None: # base case
                return
            dfs(node.left) # go left
            result.append(node.val) # visit root
            dfs(node.right) # go righht
        
        dfs(root)
        return result      

# Example usage
if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    solution = Solution()
    print(solution.inorderTraversal(root))