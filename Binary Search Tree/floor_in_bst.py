# You are given a root binary search tree and an integer x . Your task is to find the Ceil of x in the tree.
# Note: Ceil(x) is a number that is either equal to x or is immediately greater than x.
# If Ceil could not be found, return -1.

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None 

        
class Solution:
    def findFloor(self,root, x):
        floor = -1
        while root:
            if root.data <= x:
                floor = root.data
                root = root.right
            else:
                root = root.left
        return floor

if __name__ == "__main__":
    root = Node(4)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(1)
    root.left.right = Node(3)
    
    sol = Solution()
    x = 8
    print(sol.findFloor(root, x))