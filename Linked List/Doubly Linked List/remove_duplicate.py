# Given a doubly linked list of n nodes sorted by values, the task is to remove duplicate nodes present in the linked list.

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.prev = None

class Solution:
    def removeDuplicates(self, head):
        curr = head
        while curr:
            if curr.prev and curr.prev.data == curr.data:
                if curr.prev == head:
                    curr.prev = None
                    head = curr
                else:
                    curr.prev.prev.next = curr
                    curr.prev = curr.prev.prev
            curr = curr.next
        return head

# Example usage
if __name__ == "__main__":
    # Create a sorted doubly linked list: 2 <-> 2 <-> 3 <-> 4 <-> 4 <-> 4 <-> 5 <-> 5
    head = Node(2)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(4)
    sixth = Node(4)
    seventh = Node(5)
    eighth = Node(5)

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

    # Helper to print the list
    def printList(node):
        while node:
            print(node.data, end=" <-> " if node.next else "\n")
            node = node.next

    print("Original Doubly Linked List:")
    printList(head)

    # Remove duplicates
    sol = Solution()
    new_head = sol.removeDuplicates(head)

    print("\nList after removing duplicates:")
    printList(new_head)
