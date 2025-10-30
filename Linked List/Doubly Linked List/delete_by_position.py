# You are given a Doubly Linked List and an integer x. Remove the node at position x (positions are 1-indexed) from the list, and return the head of the updated list.

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Solution:
    def delete_by_position(self, head: Node, position: int) -> Node:
        # If the list is empty
        if head is None:
            print("❌ List is empty!")
            return head
        
        # If the head needs to be removed
        if position == 1:
            new_head = head.next
            if new_head:
                new_head.prev = None
            return new_head
        
        current = head
        count = 1
        
        # Traverse to the node at the given position
        while current is not None and count < position:
            current = current.next
            count += 1
        
        # If the position is more than the number of nodes
        if current is None:
            print("Position out of bounds")
            return head
        
        # If it's the last node
        if current.next is None:  
            current.prev.next = None
        else:
            current.prev.next = current.next
            current.next.prev = current.prev
        return head
    
# Example usage:
if __name__ == "__main__":
    # Creating a doubly linked list: 1 <-> 2 <-> 3 <-> 4 <-> 5
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    head.next = second
    second.prev = head
    second.next = third
    third.prev = second
    third.next = fourth
    fourth.prev = third
    fourth.next = fifth
    fifth.prev = fourth

    position = 3  # Remove the node at position 3

    solution = Solution()
    new_head = solution.delete_by_position(head, position)

    # Printing the modified doubly linked list
    current = new_head
    while current:
        print(current.data, end=" <-> " if current.next else "")
        current = current.next
    # Output should be: 1 <-> 2 <-> 4 <-> 5