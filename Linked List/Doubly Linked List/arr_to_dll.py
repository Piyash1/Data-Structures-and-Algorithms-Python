# Given an integer array arr of size n. Construct the doubly linked list from arr and return the head of it.

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.prev = None

class Solution:
    def constructDLL(self, arr):
        # Code here
        if len(arr) == 0:
            return None
        
        head = Node(arr[0])
        prev_node = head
        
        for i in range(1, len(arr)):
            new_node = Node(arr[i])
            
            prev_node.next = new_node
            new_node.prev = prev_node
            
            prev_node = new_node
        return head

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    arr = [1,2,3,4,5]
    head = solution.constructDLL(arr)
    
    # Print the updated list
    current = head
    while current is not None:
        print(current.data, end=" <-> " if current.next else "")
        current = current.next