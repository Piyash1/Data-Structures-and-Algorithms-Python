# Implement a Stack using a Linked List, this stack has no fixed capacity and can grow dynamically until memory is available.

# Node class
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.prev = None  # Add this for doubly linked list
        self.next = None 

# Stack class template
class myStack:
    def __init__(self):
        # Initialize your data members
        self.head = None
        self.tail = None
        self.stack_size = 0
        
    def isEmpty(self):
        # Check if the stack is empty
        return self.head is None
        
    def push(self, x):
        # Adds element x to the top of the stack
        new_node = Node(x)
        if self.tail is None:  # Empty stack
            self.head = self.tail = new_node  
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.stack_size += 1
        
    def pop(self):
        # Removes an element from the top of the stack
        if self.tail is None:
            return -1
        if self.head == self.tail:  # Only one element
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.stack_size -= 1
        
    def peek(self):
        # Returns the top element of the stack
        # If the stack is empty, return -1
        if self.tail is None:
            return -1
        return self.tail.data
        
    def size(self):
        # Returns the current size of the stack
        return self.stack_size


# Test the corrected code
stack = myStack()

print("Testing Stack Operations:")
print(f"isEmpty(): {stack.isEmpty()}")  # True

stack.push(5)
print(f"After push(5) - peek(): {stack.peek()}, size(): {stack.size()}")  # 5, 1

stack.push(3)
print(f"After push(3) - peek(): {stack.peek()}, size(): {stack.size()}")  # 3, 2

stack.push(4)
print(f"After push(4) - peek(): {stack.peek()}, size(): {stack.size()}")  # 4, 3

stack.pop()
print(f"After pop() - peek(): {stack.peek()}, size(): {stack.size()}")  # 3, 2

print(f"isEmpty(): {stack.isEmpty()}")  # False