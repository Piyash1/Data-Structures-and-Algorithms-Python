#  Morris Algorithm for Inorder/Preorder Traversal

class TreeNode:
    def __init__(self, val):
        self.right = None
        self.val = val
        self.left = None 

class Solution:
    def inorderTraversal(self, root):
        result = []
        current = root
        
        while current:
            if current.left is None:
                result.append(current.val)
                current = current.right
            else:
                predecessor = current.left
                
                while predecessor.right is not None and predecessor.right != current:
                    predecessor = predecessor.right
                if predecessor.right is None:
                    predecessor.right = current
                    current = current.left
                else:
                    predecessor.right = None
                    result.append(current.val)
                    current = current.right
        return result
    
    
    # PreOrder
    def preorderTraversal(self, root):
        result = []
        current = root
        
        while current:
            if current.left is None:
                result.append(current.val)
                current = current.right
            else:
                predecessor = current.left
                
                while predecessor.right is not None and predecessor.right != current:
                    predecessor = predecessor.right
                if predecessor.right is None:
                    result.append(current.val)
                    predecessor.right = current
                    current = current.left
                else:
                    predecessor.right = None
                    current = current.right
        return result

# Example usage
if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    solution = Solution()
    inorder = solution.inorderTraversal(root)
    print(f"Inorder Traversal: {inorder}")
    
    preorder = solution.preorderTraversal(root)
    print(f"Preorder Traversal: {preorder}")