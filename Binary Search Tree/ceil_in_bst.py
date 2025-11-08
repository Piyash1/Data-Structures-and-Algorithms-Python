# You are given a root binary search tree and an integer x . Your task is to find the Ceil of x in the tree.
# Note: Ceil(x) is a number that is either equal to x or is immediately greater than x.
# If Ceil could not be found, return -1.

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None 

        
class Solution:
    def findCeil(self,root, x):
        ceil = -1
        while root:
            if root.data == x:
                return root.data
            elif root.data < x:
                root = root.right
            else:
                ceil = root.data
                root = root.left
        return ceil

if __name__ == "__main__":
    root = Node(4)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(1)
    root.left.right = Node(3)
    
    sol = Solution()
    x = 3
    print(sol.findCeil(root, x))