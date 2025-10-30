# Leetcode no.142 - Linked List Cycle II

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
    
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
    cycle_start_node = solution.detectCycle(node1)
    if cycle_start_node:
        print(f"Cycle starts at node with value: {cycle_start_node.val}")
    else:
        print("No cycle detected.")
        

# # Brute Force Approach:
# class Solution:
#     def detectCycle(self, head: ListNode) -> ListNode:
#         if not head:
#             return None
        
#         curr = head
#         my_set = set()
#         while curr:
#             if curr in my_set:
#                 return curr
#             my_set.add(curr)
#             curr = curr.next
#         return None