class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_head(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
    
    def insert_at_position(self, data, position):
        if position == 0:
            self.insert_at_head(data)
            return
        new_node = Node(data)
        current = self.head
        count = 0
        while current and count < position - 1:
            current = current.next
            count += 1
        if current is None:
            print("Position out of bounds")
            return
        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node
        
    def delete_node(self, key):
        # step 1: check if list is empty
        if self.head is None:
            print("❌ List is empty!")
            return
        
        # step 2: traverse the list to find the node to delete
        current = self.head
        while current is not None:
            if current.data == key:
                print(f"\nDeleting node with value: {key}")
                
                # if its the first node
                if current.prev is None:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                elif current.next is None:  # if its the last node
                    current.prev.next = None
                else:  # if its a middle node
                    current.prev.next = current.next
                    current.next.prev = current.prev
                print(f"✅ Successfully deleted {key}")
                return
            current = current.next
        print(f"❌ Node with value {key} not found!")
                
                
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> " if current.next else "")
            current = current.next
        print()

# Example usage:
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(10)
    dll.append(20)
    dll.insert_at_head(5)
    dll.append(30)
    dll.insert_at_position(15, 2)  # Insert 15 at position 2
    print("\nDoubly Linked List after insertions:")
    dll.display()  
    
    dll.delete_node(20)  # Delete node with value 20
    print("\nAfter deletion:")
    dll.display()
