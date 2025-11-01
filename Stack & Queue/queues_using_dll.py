# Implement a Queue using a Linked List, this queue has no fixed capacity and can grow dynamically until memory is available.

class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.prev = None
        self.next = None

# Queue class using Doubly Linked List
class myQueue:
    def __init__(self):
        # Initialize head (front) and tail (rear)
        self.head = None  # Front of queue (dequeue from here)
        self.tail = None  # Rear of queue (enqueue here)
        self.queue_size = 0
    
    def isEmpty(self):
        """Check if the queue is empty"""
        return self.head is None
    
    def enqueue(self, x):
        """Add element x to the rear of the queue"""
        new_node = Node(x)
        if self.tail is None:  # Empty queue
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.queue_size += 1
    
    def dequeue(self):
        """Remove element from the front of the queue"""
        if self.head is None:  # Empty queue
            return -1
        removed_value = self.head.data
        if self.head == self.tail:  # Only one element
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.queue_size -= 1
        return removed_value
    
    def front(self):
        """Return front element without removing it"""
        if self.head is None:
            return -1
        return self.head.data
    
    def rear(self):
        """Return rear element without removing it"""
        if self.tail is None:
            return -1
        return self.tail.data
    
    def size(self):
        """Return the current size of the queue"""
        return self.queue_size
    
    def display(self):
        """Display all elements in the queue (front to rear)"""
        if self.head is None:
            print("Queue is empty")
            return
        temp = self.head
        elements = []
        while temp:
            elements.append(temp.data)
            temp = temp.next
        print(f"Queue (front -> rear): {elements}")


# Test the Queue
print("="*60)
print("Queue Operations using Doubly Linked List")
print("="*60)

queue = myQueue()

print("\n1. Check if empty:")
print(f"isEmpty(): {queue.isEmpty()}")  # True

print("\n2. Enqueue elements:")
queue.enqueue(10)
print(f"Enqueued 10")
queue.display()

queue.enqueue(20)
print(f"Enqueued 20")
queue.display()

queue.enqueue(30)
print(f"Enqueued 30")
queue.display()

queue.enqueue(40)
print(f"Enqueued 40")
queue.display()

print(f"\nFront: {queue.front()}, Rear: {queue.rear()}, Size: {queue.size()}")

print("\n3. Dequeue elements:")
print(f"Dequeued: {queue.dequeue()}")
queue.display()

print(f"Dequeued: {queue.dequeue()}")
queue.display()

print(f"\nFront: {queue.front()}, Rear: {queue.rear()}, Size: {queue.size()}")