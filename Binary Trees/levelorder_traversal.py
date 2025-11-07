# Leetcode no.102 - Binary Tree Level Order Traversal

from collections import deque
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        result = []
        queue = deque([])
        queue.append(root)
        
        while len(queue) != 0:
            level_size = len(queue)
            current_level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            result.append(current_level)
            
        return result

# Example usage

    #         1
    #        / \
    #       2   3
    #      / \   \
    #     4   5   6
    #    /
    #   7

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    root.left.left.left = TreeNode(7)
    
    sol = Solution()
    result = sol.levelOrder(root)
    print(result)