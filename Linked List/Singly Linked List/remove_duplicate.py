# Leetcode no.83 - Remove Duplicates from Sorted List

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def deleteDuplicates(self, head):
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
    
# Example usage:
if __name__ == "__main__":
    # Creating sorted linked list with duplicates: 1 -> 1 -> 2 -> 3 -> 3
    head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))    
    solution = Solution()
    unique_list = solution.deleteDuplicates(head)
    
    # Print linked list after removing duplicates
    current = unique_list
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next