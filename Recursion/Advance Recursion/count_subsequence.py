class Solution:
    def backtrack(self, nums, index, total, k):
        # Base case: We've considered all elements
        if index >= len(nums):  # We are going till end because this array may contain zeros
            if total == k:
                return 1  # Valid subsequence found
            return 0  # Not valid
            
        # Choice 1: Include the current element
        Sum = total + nums[index]
        left = self.backtrack(nums, index + 1, Sum, k)
        
        # Choice 2: Exclude the current element
        Sum = total
        right = self.backtrack(nums, index + 1, Sum, k)
        
        # Return total count from both choices
        return left + right
        
    def perfectSum(self, arr, target):
        return self.backtrack(arr, 0, 0, target)

# Example usage:
if __name__ == "__main__":
    arr = [1, 2, 3]
    target = 3
    sol = Solution()
    result = sol.perfectSum(arr, target)
    print(result)  # Output: Number of subsequences summing to target