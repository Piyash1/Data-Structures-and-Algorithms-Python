# Given a sorted doubly linked list of positive distinct elements, the task is to find pairs in a doubly-linked list whose sum is equal to given value target.
from typing import Optional
from typing import List

class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
        self.prev=None

class Solution:
    def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        left = head
        right = head
        result = []
        
        while right.next:
            right = right.next
        
        while left is not None and right is not None and left.data < right.data:
            total = left.data + right.data
            if total == target:
                result.append([left.data, right.data])
                left = left.next
                right = right.prev
            elif total > target:
                right = right.prev
            else:
                left = left.next
        return result

# Example usage
if __name__ == "__main__":
    # Create doubly linked list manually: 2 <-> 2 <-> 10 <-> 8 <-> 4 <-> 2 <-> 5 <-> 2
    head = Node(1)
    second = Node(2)
    third = Node(4)
    fourth = Node(5)
    fifth = Node(6)
    sixth = Node(8)
    seventh = Node(9)

    # Linking nodes
    head.next = second
    second.prev = head
    second.next = third
    third.prev = second
    third.next = fourth
    fourth.prev = third
    fourth.next = fifth
    fifth.prev = fourth
    fifth.next = sixth
    sixth.prev = fifth
    sixth.next = seventh
    seventh.prev = sixth

    # Function to print the list
    def printList(node):
        while node:
            print(node.data, end=" <-> " if node.next else "\n")
            node = node.next

    print("Original list:")
    printList(head)

    # Find pairs with given sum
    target = 7
    sol = Solution()
    pairs = sol.findPairsWithGivenSum(target, head)

    print(f"\nPairs with sum {target}:")
    for pair in pairs:
        print(pair)
        
        
