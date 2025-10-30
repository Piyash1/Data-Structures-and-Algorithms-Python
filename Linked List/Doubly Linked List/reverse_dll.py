# You are given the head of a doubly linked list. You have to reverse the doubly linked list and return its head.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Solution:
    def reverseDLL(self, head: Node) -> Node:
        if head.next is None:
            return head
        curr = head
        prev = None
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            curr.prev = next_node
            prev = curr
            curr = next_node
        return prev

# Example usage:
if __name__ == "__main__":
    # Creating a doubly linked list: 1 <-> 2 <-> 3 <-> 4 <-> 5
    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    head.next.next = Node(3)
    head.next.next.prev = head.next
    head.next.next.next = Node(4)
    head.next.next.next.prev = head.next.next
    head.next.next.next.next = Node(5)
    head.next.next.next.next.prev = head.next.next.next

    solution = Solution()
    new_head = solution.reverseDLL(head)

    # Printing the reversed doubly linked list
    current = new_head
    while current:
        print(current.data, end=" <-> " if current.next else "")
        current = current.next
    # Output should be: 5 <-> 4 <-> 3 <-> 2 <-> 1