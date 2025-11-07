# Leetcode np.104 - Maximum Depth of Binary Tree

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Reccursive DFS Approach     
class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        return 1 + max(left_depth, right_depth)
        
# Example usage
if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    sol = Solution()
    print(sol.maxDepth(root))
    
    
# # Iterative BFS Approach
# class Solution(object):
#     def maxDepth(self, root):
#         if root is None:
#             return 0
#         from collections import deque
#         queue = deque([root])
#         depth = 0
        
#         while len(queue) != 0:
#             depth += 1
#             level_size = len(queue)
            
#             for _ in range(level_size):
#                 node = queue.popleft()
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#         return depth
