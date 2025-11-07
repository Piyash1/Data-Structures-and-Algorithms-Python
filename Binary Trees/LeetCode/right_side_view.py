# Leetcode no.199 - Binary Tree Right Side View

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS Approach      
class Solution(object):
    def rightSideView(self, root):
        ans = []
        self.dfs(root, 0, ans)
        return ans
    
    def dfs(self, node, depth, ans):
        if not node:
            return None
        if len(ans) == depth:
            ans.append(node.val)
        if node.right:
            self.dfs(node.right, depth + 1, ans)
        if node.left:
            self.dfs(node.left, depth + 1, ans)
    
# Example usage
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    root.left.right = TreeNode(5)
    
    sol = Solution()
    print(sol.rightSideView(root))
    

# # BFS Approach      
# from collections import deque
# class Solution(object):
#     def rightSideView(self, root):
#         if not root:
#             return 
#         result = []
#         queue = deque([root])
        
#         while queue:
#             level_size = len(queue)
#             for i in range(level_size):
#                 node = queue.popleft()
#                 if i == level_size - 1:
#                     result.append(node.val)
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#         return result