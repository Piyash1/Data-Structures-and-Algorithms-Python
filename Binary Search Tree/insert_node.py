# Leetcode no.701 - Insert into a Binary Search Tree

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def insertIntoBST(self, root, val):
        if root is None:
            return TreeNode(val)
        temp = root
        while True:
            if val < temp.val:
                if temp.left is None:
                    temp.left = TreeNode(val)
                    break
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = TreeNode(val)
                    break
                temp = temp.right
        return root

# Example usage
if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    
    sol = Solution()
    new_root = sol.insertIntoBST(root, 5)
    
    # Helper function to print tree (inorder traversal)
    def inorder(node):
        if not node:
            return []
        return inorder(node.left) + [node.val] + inorder(node.right)
    
    print("Inorder traversal:", inorder(new_root))  # [1, 2, 3, 4, 5, 7]