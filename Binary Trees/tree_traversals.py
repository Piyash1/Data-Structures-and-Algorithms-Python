# Given a binary tree, return its inorder, preorder, and postorder traversals.

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def getTreeTraversal(root):
    inorder = []
    preorder = []
    postorder = []
    
    def inorderTraversal(node):
        if not node:
            return
        inorderTraversal(node.left)
        inorder.append(node.data)
        inorderTraversal(node.right)
    
    def preorderTraversal(node):
        if not node:
            return
        preorder.append(node.data)
        preorderTraversal(node.left)
        preorderTraversal(node.right)
    
    def postorderTraversal(node):
        if not node:
            return
        postorderTraversal(node.left)
        postorderTraversal(node.right)
        postorder.append(node.data)
        
    inorderTraversal(root)
    preorderTraversal(root)
    postorderTraversal(root)
    
    return[inorder, preorder, postorder]

# Test example
if __name__ == "__main__":
    # Create a sample tree:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    result = getTreeTraversal(root)
    print("Inorder:", result[0])    # [4, 2, 5, 1, 3]
    print("Preorder:", result[1])   # [1, 2, 4, 5, 3]
    print("Postorder:", result[2])  # [4, 5, 2, 3, 1]