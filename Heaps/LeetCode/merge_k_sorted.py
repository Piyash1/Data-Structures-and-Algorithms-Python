# Leetcode no.23 - Merge k Sorted Lists

import heapq

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return None
        
        # Min-heap
        min_heap = []

        # Step 1: Put the first node of each list into the heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))
        
        # Dummy node to build result
        dummy = ListNode()
        current = dummy

        # Step 2: Process until heap is empty
        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            
            # Add the smallest node to our result
            current.next = node
            current = current.next

            # If the popped node has a next → push it into the heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))

        return dummy.next


# Example usage
if __name__ == "__main__":
    sol = Solution()
    # Creating example linked lists
    l1 = ListNode(1, ListNode(4, ListNode(5)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    l3 = ListNode(2, ListNode(6))
    lists = [l1, l2, l3]
    
    merged_head = sol.mergeKLists(lists)
    
    # Print merged linked list
    current = merged_head
    merged_list = []
    while current:
        merged_list.append(current.val)
        current = current.next
    print("Merged sorted linked list:", merged_list)
            
       
        
        
        