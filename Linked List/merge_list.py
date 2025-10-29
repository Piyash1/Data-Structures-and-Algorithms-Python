# Leetcode no.21 - Merge Two Sorted Lists

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        current = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        return dummy.next

# Example usage:
if __name__ == "__main__":
    # Creating first sorted linked list: 1 -> 2 -> 4
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    
    # Creating second sorted linked list: 1 -> 3 -> 4
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    
    solution = Solution()
    merged_list = solution.mergeTwoLists(list1, list2)
    
    # Print merged linked list
    current = merged_list
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next    