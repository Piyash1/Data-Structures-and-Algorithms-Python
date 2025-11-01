# Leetcode no.232 - Implement Queue using Stacks

class MyQueue(object):

    def __init__(self):
        self.st1 = []
        self.st2 = []

    def push(self, x):
        while self.st1:
            self.st2.append(self.st1.pop())
        self.st1.append(x)
        while self.st2:
            self.st1.append(self.st2.pop())
        
    def pop(self):
        if not self.st1:
            print("Queue is empty")
            return -1
        return self.st1.pop()
        
    def peek(self):
        if not self.st1:
            print("Queue is empty")
            return -1
        return self.st1[-1]
    
    def empty(self):
        return not self.st1
    

# Example Usage
print("=== Creating Queues ===")
queue = MyQueue()

print("\n=== Pushing elements ===")
queue.push(1)
print(f"Pushed 1, peek is: {queue.peek()}")

queue.push(2)
print(f"Pushed 2, peek is: {queue.peek()}")

queue.push(3)
print(f"Pushed 3, peek is: {queue.peek()}")

print("\n=== Checking peek element ===")
print(f"peek element: {queue.peek()}")  # Should be 3 (last pushed)

print("\n=== Popping elements ===")
print(f"Popped: {queue.pop()}")  # Should pop 3
print(f"peek after pop: {queue.peek()}")  # Should be 2

print(f"Popped: {queue.pop()}")  # Should pop 2
print(f"Popped: {queue.pop()}")  # Should pop 1

print("\n=== Checking if empty ===")
print(f"Is queue empty? {queue.empty()}")  # Should be True

print("\n=== Trying to pop from empty queue ===")
result = queue.pop()  # Should print "queue is empty"
print(f"Result: {result}")
        
