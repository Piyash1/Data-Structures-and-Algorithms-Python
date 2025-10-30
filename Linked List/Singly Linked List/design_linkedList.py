# Leetcode 707: Design Linked List

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1

        current = self.head

        for _ in range(0, index):
            current = current.next

        return current.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be
        the first node of the linked list.
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked
        list, the node will be appended to the end of linked list. If index is greater than the length, the node will not
        be inserted.
        """
        if index > self.size:
            return

        current = self.head
        new_node = ListNode(val)

        if index <= 0:
            new_node.next = current
            self.head = new_node
        else:
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

        self.size += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return

        current = self.head

        if index == 0:
            self.head = self.head.next
        else:
            for _ in range(0, index - 1):
                current = current.next
            current.next = current.next.next

        self.size -= 1
        
    def display(self):
        """
        Display the contents of the linked list as a space-separated string.
        Returns an empty string if the list is empty.
        """
        if self.size == 0:
            return "[]"

        current = self.head
        values = []
        while current:
            values.append(str(current.val))
            current = current.next
        return f"[{ ' '.join(values) }]"


# Example usage of MyLinkedList class with display method
my_list = MyLinkedList()

print(my_list.display())  # Output: []

# Add nodes
my_list.addAtHead(1)      # List: [1]
print(my_list.display())  # Output: [1]

my_list.addAtTail(3)      # List: [1, 3]
print(my_list.display())  # Output: [1 3]

my_list.addAtIndex(1, 2)  # List: [1, 2, 3]
print(my_list.display())  # Output: [1 2 3]

# Get values
print(my_list.get(0))     # Output: 1
print(my_list.get(2))     # Output: 3

# Delete nodes
my_list.deleteAtIndex(1)  # List: [1, 3]
print(my_list.display())  # Output: [1 3]

my_list.deleteAtIndex(1)  # List: [1]
print(my_list.display())  # Output: [1]

my_list.deleteAtIndex(0)  # List: []
print(my_list.display())  # Output: []

print(my_list.get(1))     # Output: -1 (invalid index)