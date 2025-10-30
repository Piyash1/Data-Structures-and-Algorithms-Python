# Given the head of a doubly-linked list, a position p, and an integer x. Add a new node with value x at the position just after pth node in the doubly linked list and return the head of the updated list.
# Note: The position is 0-based indexed.

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Solution:
    def insertAfterPosition(self, head, p, x):
        new_node = Node(x)
        
        # If the list is empty
        if head is None:
            return new_node
        
        current = head
        count = 0
        
        # Traverse to the pth node
        while current is not None and count < p:
            current = current.next
            count += 1
        
        if current is None:
            return head  # Position p is out of bounds
        
        new_node.next = current.next
        new_node.prev = current
        if current.next is not None:
            current.next.prev = new_node
        current.next = new_node
        return head

# Example usage:
if __name__ == "__main__":
    # Creating a doubly linked list: 1 <-> 2 <-> 3
    head = Node(1)
    second = Node(2)
    third = Node(3)
    
    head.next = second
    second.prev = head
    second.next = third
    third.prev = second
    
    solution = Solution()
    p = 1  # Position after which to insert
    x = 4  # Value to insert
    
    updated_head = solution.insertAfterPosition(head, p, x)
    
    # Print the updated list
    current = updated_head
    while current is not None:
        print(current.data, end=" <-> " if current.next else "")
        current = current.next