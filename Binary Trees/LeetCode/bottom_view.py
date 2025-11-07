# You are given the root of a binary tree, and your task is to return its top view. The top view of a binary tree is the set of nodes visible when the tree is viewed from the top.

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

from collections import deque
class Solution:
    def bottomView(self, root):
        if not root:
            return None
        result = []
        queue = deque()
        my_dict = {}
        
        queue.append((root, 0))
        while queue:
            node, line = queue.popleft()
            my_dict[line] = node.data
            if node.left:
                queue.append((node.left, line - 1))
            if node.right:
                queue.append((node.right, line + 1))
        
        for value in sorted(my_dict.items()):
            result.append(value[1])
        return result

# Example usage
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    
    sol = Solution()
    print(sol.bottomView(root))
        
        
        