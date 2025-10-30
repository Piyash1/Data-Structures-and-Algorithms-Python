# Given the head of a linked list, determine whether the list contains a loop. If a loop is present, return the number of nodes in the loop, otherwise return 0.

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution:
    def length_of_loop(self, head: ListNode) -> int:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # Loop detected, now count the number of nodes in the loop
                slow = slow.next
                count = 1
                while slow != fast:
                    slow = slow.next
                    count += 1
                return count
        return 0
    
# Example usage:
if __name__ == "__main__":
    # Creating a linked list with a loop for testing
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node3  # Creates a loop here

    solution = Solution()
    print(solution.length_of_loop(node1))  # Output: 3 (nodes 3, 4, 5 form the loop)
    
    
    
    # # Brute Force Approach
    # class Solution:
    # def length_of_loop(self, head: ListNode) -> int:
    #     curr = head
    #     my_dict = dict()
    #     travel = 0
    #     while curr:
    #         if curr in my_dict:
    #             return travel - my_dict[curr]
    #         my_dict[curr] = travel
    #         travel += 1
    #         curr = curr.next
    #     return 0