# Leetcode no.2807 - Insert Greatest Common Divisors in Linked List

class  ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: ListNode) -> ListNode:
        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a
        
        if not head:
            return head
        
        prev = head
        curr = head.next

        while curr:
            gcd_val = gcd(prev.val, curr.val)  # Use custom gcd
            g = ListNode(gcd_val)
            prev.next = g
            g.next = curr
            prev = curr
            curr = curr.next
        return head

# Example usage:
if __name__ == "__main__":
    # Create a linked list 12 -> 15 -> 18
    head = ListNode(12, ListNode(15, ListNode(18)))
    
    solution = Solution()
    new_head = solution.insertGreatestCommonDivisors(head)
    
    # Print the modified linked list
    curr = new_head
    while curr:
        print(curr.val, end=" -> " if curr.next else "")
        curr = curr.next
    # Expected output: 12 -> 3 -> 15 -> 3 -> 18