# Step 1: Create a Node class
class Node:
    def __init__(self, data):
        self.data = data    # store data
        self.next = None    # pointer to the next node

# Step 2: Create LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None    # start of the list (initially empty)

    # Add new node at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:          # if list is empty
            self.head = new_node
            return
        current = self.head
        while current.next:        # move until last node
            current = current.next
        current.next = new_node    # link last node to new node
    
    # Insert at specific position
    def insert_at_position(self, data, position):
        new_node = Node(data)
        if position == 0:          # insert at head
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        prev_node = None
        count = 0
        while current is not None and count < position:
            prev_node = current
            current = current.next
            count += 1
        prev_node.next = new_node
        new_node.next = current
    
    # Delete node by value
    def delete_by_value(self, value):
        # Case 1: Empty list
        if not self.head:
            print("❌ List is empty!")
            return
        
        # Case 2: Deleting head node
        if self.head.data == value:
            self.head = self.head.next
            return
        
        # Case 3: Search and delete in the middle/end
        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next
        

    # Display the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Step 3: Use the LinkedList
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)

print("\nInitial linked list:")
linked_list.display()

linked_list.insert_at_position(15, 1)
print("\nLinked list after inserting 15 at position 1:")
linked_list.display()

linked_list.delete_by_value(20)
print("\nLinked list after deleting value 20:")
linked_list.display()


