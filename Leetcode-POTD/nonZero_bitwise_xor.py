# 3702. Longest Subsequence With Non-Zero Bitwise XOR
# 
# Problem: Find the longest subsequence where XOR of all elements is non-zero
# 
# Key Insight: 
#   - If XOR of all elements is non-zero, we can take the entire array
#   - If XOR of all elements is zero, we need to exclude at least one element
#   - To get non-zero XOR when all XOR is 0, remove any one non-zero element

from typing import List

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Step 1: Calculate XOR of all elements in the array
        xor = 0
        for num in nums:
            xor ^= num
        
        # Step 2: If XOR of all elements is non-zero, we can include all elements
        if xor != 0:
            return n
        
        # Step 3: If XOR is zero, we need to remove one element to get non-zero XOR
        # Find if there's any non-zero element that we can exclude
        for num in nums:
            if num != 0:
                # If we find any non-zero element, remove it and return n-1
                # (Removing a non-zero element from an all-zero XOR will give non-zero)
                return n - 1
        
        # Step 4: If all elements are zero, XOR will always be 0, so return 0
        # (No valid subsequence exists with non-zero XOR)
        return 0

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    # Example: [1, 2, 3] -> XOR = 1^2^3 = 0, has non-zero elements, so return 2
    nums = [1, 2, 3]
    print(solution.longestSubsequence(nums))  # Output: 2