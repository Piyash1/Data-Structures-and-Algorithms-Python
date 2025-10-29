class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.items[0]
    
    def rear(self):
        if self.is_empty():
            raise IndexError("rear from empty queue")
        return self.items[-1]

    def size(self):
        return len(self.items)
    
queue = Queue()

queue.enqueue(5)
queue.enqueue(10)
queue.enqueue(15)
queue.enqueue(20)
print("\nQueue contents:", queue.items)

queue.dequeue()
print("\nQueue contents after dequeue:", queue.items)

queue.front()
print("\nFront element is:", queue.front())

queue.rear()
print("\nRear element is:", queue.rear())

queue.size()
print("\nQueue size is:", queue.size())

queue.is_empty()
print("\nQueue is empty")