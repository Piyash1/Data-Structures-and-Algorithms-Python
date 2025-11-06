# Leetcode no.144 - Binary Tree Preorder Traversal

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def preorderTraversal(self, root):
        result = []
        
        def dfs(node):
            if node == None:
                return
            result.append(node.val)
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return result
           
# Example usage
if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    solution = Solution()
    print(solution.preorderTraversal(root))
        