# Leetcode no.328 - Odd Even Linked List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        odd = head
        even = head.next
        even_head = even
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = even_head
        return head

# Example usage:
if __name__ == "__main__":
    # Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    solution = Solution()
    new_head = solution.oddEvenList(head)

    # Printing the modified linked list
    current = new_head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    # Output should be: 1 -> 3 -> 5 -> 2 -> 4
    
    
    
    # #Brute Force Approach
    # class Solution:
    # def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if head is None or head.next is None:
    #         return head  # Empty list or single node - nothing to rearrange

    #     temp = head
    #     values = []

    #     # First pass: Collecting values from odd-indexed nodes (1st, 3rd, 5th, ...)
    #     while temp:
    #         values.append(temp.val)  # Add current node's value
    #         if temp.next:
    #             temp = temp.next.next  # Skip one node to get next odd position
    #         else:
    #             break  # Reached end of list

    #     temp = head.next  # Start from 2nd node (first even position)

    #     # Second pass: Collecting values from even-indexed nodes (2nd, 4th, 6th, ...)
    #     while temp:
    #         values.append(temp.val)  # Add current node's value
    #         if temp.next:
    #             temp = temp.next.next  # Skip one node to get next even position
    #         else:
    #             break  # Reached end of list

    #     # Third pass: Assigning collected values back to the nodes
    #     index = 0
    #     temp = head
    #     while temp:
    #         temp.val = values[index]  # Replace node value with rearranged value
    #         index += 1
    #         temp = temp.next

    #     return head
       