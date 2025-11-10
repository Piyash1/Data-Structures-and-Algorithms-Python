# Leetcode no.230 - Kth Smallest Element in a BST

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """
        1. Add a counter to track visited nodes
        2. Return immediately when count reaches k
        """
        current = root
        count = 0
        
        while current:
            if current.left is None:
                # Visit this node
                count += 1
                if count == k:
                    return current.val
                current = current.right
            else:
                # Find the inorder predecessor
                predecessor = current.left
                
                while predecessor.right is not None and predecessor.right != current:
                    predecessor = predecessor.right
                
                if predecessor.right is None:
                    # Create thread
                    predecessor.right = current
                    current = current.left
                else:
                    # Remove thread and visit node
                    predecessor.right = None
                    count += 1
                    if count == k:
                        return current.val
                    current = current.right
        
        return -1  # Should never reach here if k is valid


# Test cases
def test_solution():
    sol = Solution()
    
    # Test case 1: [3,1,4,null,2], k = 1
    root1 = TreeNode(3)
    root1.left = TreeNode(1)
    root1.right = TreeNode(4)
    root1.left.right = TreeNode(2)
    print(f"Test 1 (k=1): {sol.kthSmallest(root1, 1)}")  # Expected: 1
    
    # Test case 2: [5,3,6,2,4,null,null,1], k = 3
    root2 = TreeNode(5)
    root2.left = TreeNode(3)
    root2.right = TreeNode(6)
    root2.left.left = TreeNode(2)
    root2.left.right = TreeNode(4)
    root2.left.left.left = TreeNode(1)
    print(f"Test 2 (k=3): {sol.kthSmallest(root2, 3)}")  # Expected: 3
    print(f"Test 3 (k=1): {sol.kthSmallest(root2, 1)}")  # Expected: 1
    print(f"Test 4 (k=6): {sol.kthSmallest(root2, 6)}")  # Expected: 6
    print(f"Test 5 (k=4): {sol.kthSmallest(root2, 4)}")  # Expected: 4
    
    # Test case 3: Single node
    root3 = TreeNode(1)
    print(f"Test 6 (k=1): {sol.kthSmallest(root3, 1)}")  # Expected: 1

test_solution()