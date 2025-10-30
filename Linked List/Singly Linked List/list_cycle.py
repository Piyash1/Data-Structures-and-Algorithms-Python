# Leetcode no.141 - Linked List Cycle

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False

# Example usage:
if __name__ == "__main__":
    # Creating a linked list with a cycle for testing
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Creates a cycle here

    solution = Solution()
    print(solution.hasCycle(node1))  # Output: True
    
    
    
    # # Brute Force Approach:
# class Solution:
#     def detectCycle(self, head: ListNode) -> ListNode:
#         if not head:
#             return None
        
#         curr = head
#         my_set = set()
#         while curr:
#             if curr in my_set:
#                 return True
#             my_set.add(curr)
#             curr = curr.next
#         return False