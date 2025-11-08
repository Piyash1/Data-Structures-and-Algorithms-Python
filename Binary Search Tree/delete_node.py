# Leetcode no.450 - Delete Node in a BST

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def deleteNode(self, root, key):
        
        #Base case
        if root is None:
            return None
        if root.val == key:
            return self.deletion(root)
        
        # Find the node to delete
        temp = root
        while temp:
            if temp.val > key:
                if temp.left and temp.left.val == key:
                    temp.left = self.deletion(temp.left)
                    break
                else:
                    temp = temp.left
            else:
                if temp.right and temp.right.val == key:
                    temp.right = self.deletion(temp.right)
                    break
                else:
                    temp = temp.right
        return root
    
    # Delete node -> 3 cases
    def deletion(self, node):
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        else:
            right_child = node.right
            last_right = self.find_last_right(node.left)
            last_right.right = right_child
            return node.left
    
    def find_last_right(self, node):
        while node.right:
            node = node.right
        return node


# Example usage:
if __name__ == "__main__":
    # Example: Delete 3 from tree
    #       5
    #      / \
    #     3   6
    #    / \   \
    #   2   4   7
    
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(7)
    
    sol = Solution()
    result = sol.deleteNode(root, 3)
    
    # Helper function to print tree (inorder traversal)
    def inorder(node):
        if not node:
            return []
        return inorder(node.left) + [node.val] + inorder(node.right)
    
    print("After deleting 3:", inorder(result))  # [2, 4, 5, 6, 7]