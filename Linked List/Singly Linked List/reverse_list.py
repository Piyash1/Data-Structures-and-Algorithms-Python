# Leetcode no.206 - Reverse Linked List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        prev = None
        current = head
        
        while current:
            next_node = current.next  # Store next node
            current.next = prev       # Reverse the link
            prev = current            # Move prev to current
            current = next_node       # Move to next node
            
        return prev  # New head of the reversed list
    
# Example usage:
if __name__ == "__main__":
    # Creating linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    
    solution = Solution()
    reversed_list = solution.reverseList(head)
    
    # Print reversed linked list
    current = reversed_list
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next