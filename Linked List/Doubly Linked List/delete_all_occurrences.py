# You are given the head_ref of a doubly Linked List and a Key. Your task is to delete all occurrences of the given key if it is present and return the new DLL.

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.prev = None

class Solution:
    def deleteAllOccurOfX(self, head, x):
        # If the list is empty
        if not head:
            return None
        
        curr = head
        
        # Step 1: Skip all initial nodes with value x
        while curr and curr.data == x:
            curr = curr.next
        if curr:
            curr.prev = None
        head = curr
        
        # Step 2: Traverse and delete remaining nodes
        while curr:
            if curr.data == x:
                # unlink current node
                if curr.prev:
                    curr.prev.next = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
            curr = curr.next
        
        return head

# Example usage
if __name__ == "__main__":
    # Create doubly linked list manually: 2 <-> 2 <-> 10 <-> 8 <-> 4 <-> 2 <-> 5 <-> 2
    head = Node(2)
    second = Node(2)
    third = Node(10)
    fourth = Node(8)
    fifth = Node(4)
    sixth = Node(2)
    seventh = Node(5)
    eighth = Node(2)

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
    seventh.next = eighth
    eighth.prev = seventh

    # Function to print the list
    def printList(node):
        while node:
            print(node.data, end=" <-> " if node.next else "\n")
            node = node.next

    print("Original list:")
    printList(head)

    # Delete all occurrences of x
    x = 2
    sol = Solution()
    new_head = sol.deleteAllOccurOfX(head, x)

    print(f"\nList after deleting all occurrences of {x}:")
    printList(new_head)