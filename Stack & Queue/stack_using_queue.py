# Leetcode no.225 - Implement Stack using Queues

from collections import deque

class MyStack(object):

    def __init__(self):
        self.queue = deque()

    def push(self, x):
        self.queue.append(x)
        for _ in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())     

    def pop(self):
        if len(self.queue) == 0:
            print("Stack is empty")
            return None
        return self.queue.popleft()
    
    def top(self):
        if len(self.queue) == 0:
            print("Stack is empty")
            return None
        return self.queue[0]
        
    def empty(self):
        return len(self.queue) == 0 


# Example Usage
print("=== Creating Stack ===")
stack = MyStack()

print("\n=== Pushing elements ===")
stack.push(1)
print(f"Pushed 1, top is: {stack.top()}")

stack.push(2)
print(f"Pushed 2, top is: {stack.top()}")

stack.push(3)
print(f"Pushed 3, top is: {stack.top()}")

print("\n=== Checking top element ===")
print(f"Top element: {stack.top()}")  # Should be 3 (last pushed)

print("\n=== Popping elements ===")
print(f"Popped: {stack.pop()}")  # Should pop 3
print(f"Top after pop: {stack.top()}")  # Should be 2

print(f"Popped: {stack.pop()}")  # Should pop 2
print(f"Popped: {stack.pop()}")  # Should pop 1

print("\n=== Checking if empty ===")
print(f"Is stack empty? {stack.empty()}")  # Should be True

print("\n=== Trying to pop from empty stack ===")
result = stack.pop()  # Should print "Stack is empty"
print(f"Result: {result}")