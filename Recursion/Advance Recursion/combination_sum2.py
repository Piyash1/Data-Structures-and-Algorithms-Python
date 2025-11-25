# 40. Combination Sum II

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        self.backtrack(0, 0, [], candidates, target, result)
        return result
    
    def backtrack(self, index, total, subset, nums, target, result):
        # base case
        if total == target:
            result.append(subset.copy())
            return
        if total > target:
            return
        
        for i in range(index, len(nums)):
            # skip duplicates
            if i > index and nums[i] == nums[i - 1]:
                continue
            
            # include the current element
            subset.append(nums[i])
            self.backtrack(i + 1, total + nums[i], subset, nums, target, result)
            # backtrack
            subset.pop()

# Example usage:
if __name__ == "__main__":
    candidates = [10,1,2,7,6,1,5]
    target = 8
    sol = Solution()
    combinations = sol.combinationSum2(candidates, target)
    print(combinations)

# Brute Force Approach
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = set()
        self.solve(0, 0, [], candidates, target, result)
        return [list(tup) for tup in result]
    
    def solve(self, index, total, subset, nums, target, result):
        # base case
        if total == target:
            result.add(tuple(subset.copy()))
            return
        if total > target:
            return
        if index >= len(nums):
            return
        
        # choice to include the current element
        Sum = total + nums[index]
        subset.append(nums[index])
        self.solve(index + 1, Sum, subset, nums, target, result)
        
        # choice to exclude the current element
        Sum = total
        subset.pop()
        self.solve(index + 1, Sum, subset, nums, target, result)