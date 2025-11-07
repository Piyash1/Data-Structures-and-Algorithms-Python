# Leetcode no.101 - Symmetric Tree

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False
        return (self.isMirror(left.left, right.right) and 
                self.isMirror(left.right, right.left))