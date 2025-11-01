# Implement a Stack using an Array, where the size of the array, n is given.
# The Stack must support the following operations:
# (i) push(x): Insert an element x at the top of the stack.
# (ii) pop(): Remove the element from the top of the stack.
# (iii) peek(): Return the top element if not empty, else -1.
# (iv) isEmpty(): Return true if the stack is empty else return false.
# (v) isFull(): Return true if the stack is full else return false.

class myStack:
    def __init__(self, n):
        # Define Data Structures
        self.capacity = n
        self.arr = []

    def isEmpty(self):
        # Check if stack is empty
        return len(self.arr) == 0
        
    def isFull(self):
        # Check if stack is full
        return len(self.arr) == self.capacity

    def push(self, x):
        # Insert x at the top of the stack
        if not self.isFull():
            self.arr.append(x)

    def pop(self):
        # Removes an element from the top of the stack
        if not self.isEmpty():
            self.arr.pop()

    def peek(self):
        # Returns the top element of the stack
        if not self.isEmpty():
            return self.arr[-1]
        return -1

# Driver code for testing
def process_queries(n, queries):
    stack = myStack(n)
    result = []
    
    for query in queries:
        if query[0] == 1:  # push(x)
            stack.push(query[1])
        elif query[0] == 2:  # pop()
            stack.pop()
        elif query[0] == 3:  # peek()
            result.append(stack.peek())
        elif query[0] == 4:  # isEmpty()
            result.append(stack.isEmpty())
        elif query[0] == 5:  # isFull()
            result.append(stack.isFull())
    
    return result


# Test Example 1
n1 = 3
queries1 = [[1, 5], [1, 3], [3], [2], [4], [5]]
output1 = process_queries(n1, queries1)
print(f"Example 1 Output: {output1}")
# Expected: [3, False, False]