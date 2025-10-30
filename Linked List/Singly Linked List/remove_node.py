# Leetcode no.19 - Remove Nth Node From End of List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow = head
        fast = head
        for _ in range(n):
            fast = fast.next
        if fast == None:
            return head.next
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head

# Example usage:
if __name__ == "__main__":
    # Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    n = 2  # Remove the 2nd node from the end

    solution = Solution()
    new_head = solution.removeNthFromEnd(head, n)

    # Printing the modified linked list
    current = new_head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    # Output should be: 1 -> 2 -> 3 -> 5 
    
    
    # #Brute Force Approach
    # class Solution:
    # def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    #     curr = head
    #     length = 0
    #     while curr:
    #         length += 1
    #         curr = curr.next
    #     if n == length:
    #         return head.next
    #     curr = head
    #     position_to_stop = length - n
    #     count = 1
    #     while count < position_to_stop:
    #         curr = curr.next
    #         count += 1
    #     curr.next = curr.next.next
    #     return head