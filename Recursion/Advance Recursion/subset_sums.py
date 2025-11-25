# Given a array arr of integers, return the sums of all subsets in the list.  Return the sums in any order.

class Solution:
    def subsetSums(self, arr):
        result = []
        self.backtrack(0, 0, arr, result)
        return result
    
    def backtrack(self, index, total, nums, result):
        if index >= len(nums):
            result.append(total)
            return
        # include the current element
        Sum  = total + nums[index]
        self.backtrack(index + 1, Sum, nums, result)    
        # exclude the current element
        Sum = total
        self.backtrack(index + 1, Sum, nums, result)
        
# Example usage:
if __name__ == "__main__":
    arr = [2, 3]
    sol = Solution()
    subset_sums = sol.subsetSums(arr)
    print(subset_sums)