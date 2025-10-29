class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def display(self):
        return f"[{' '.join(map(str, self.items))}]"
    

stack  = Stack()

stack.push(5)
stack.push(10)
stack.push(15)
stack.push(20)
print("\nStack contents:", stack.display())

stack.pop()
print("\nStack contents after pop:", stack.display())

stack.peek()
print("\nTop element is:", stack.peek())

stack.size()
print("\nStack size is:", stack.size())

stack.is_empty()
print("\nStack is empty")

