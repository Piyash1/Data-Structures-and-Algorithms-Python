# Leetcode no.235 - Lowest Common Ancestor of a Binary Search Tree

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        return self.solve(root, p, q)
    
    def solve(self, node, p, q):
        if not node:
            return None
        if node == p or node == q:
            return node
        left = self.solve(node.left, p, q)
        right = self.solve(node.right, p, q)
        
        if left is None and right is None:
            return None
        elif left is None:
            return right
        elif right is None:
            return left
        return node

# Example usage
if __name__ == "__main__":
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    
    sol = Solution()
    node_2 = root.left
    node_8 = root.right
    lca = sol.lowestCommonAncestor(root, node_2, node_8)
    print(f"Lowest Common Ancestor: {lca.val}")
        