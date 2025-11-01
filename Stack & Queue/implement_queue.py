# Implement a Queue using an Array, where the size of the array, n is given.
# The Queue must support the following operations:

# (i) enqueue(x): Insert an element x at the rear of the queue.
# (ii) dequeue(): Remove the element from the front of the queue.
# (iii) getFront(): Return front element if not empty, else -1.
# (iv) getRear(): Return rear element if not empty, else -1.
# (v) isEmpty(): Return true if the queue is empty else return false.
# (vi) isFull(): Return true if the queue is full else return false.

class myQueue:
    def __init__(self, n):
        """
        Initialize the queue with capacity n
        """
        self.capacity = n
        self.arr = []  # Simple list to store elements
    
    def enqueue(self, x):
        """
        Insert element x at the rear of the queue
        """
        if not self.isFull():
            self.arr.append(x)
    
    def dequeue(self):
        """
        Remove the element from the front of the queue
        """
        if not self.isEmpty():
            self.arr.pop(0)
    
    def getFront(self):
        """
        Return front element if not empty, else -1
        """
        if not self.isEmpty():
            return self.arr[0]
        return -1
    
    def getRear(self):
        """
        Return rear element if not empty, else -1
        """
        if not self.isEmpty():
            return self.arr[-1]
        return -1
    
    def isEmpty(self):
        """
        Return true if the queue is empty else return false
        """
        return len(self.arr) == 0
    
    def isFull(self):
        """
        Return true if the queue is full else return false
        """
        return len(self.arr) == self.capacity


# Driver code for testing
def process_queries(n, queries):
    queue = myQueue(n)
    result = []
    
    for query in queries:
        if query[0] == 1:  # enqueue(x)
            queue.enqueue(query[1])
        elif query[0] == 2:  # dequeue()
            queue.dequeue()
        elif query[0] == 3:  # getFront()
            result.append(queue.getFront())
        elif query[0] == 4:  # getRear()
            result.append(queue.getRear())
        elif query[0] == 5:  # isEmpty()
            result.append(queue.isEmpty())
        elif query[0] == 6:  # isFull()
            result.append(queue.isFull())
    
    return result


# Test Example 1
n1 = 3
queries1 = [[1, 5], [1, 3], [1, 4], [3], [2], [5], [4]]
output1 = process_queries(n1, queries1)
print(f"Example 1 Output: {output1}")
# Expected: [5, False, 4]