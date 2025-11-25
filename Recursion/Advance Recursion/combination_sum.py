# Leetcode no.39 - Combination Sum

class Solution(object):
    def combinationSum(self, candidates, target):
        result = []
        self.solve(0, 0, [], candidates, target, result)
        return result
    
    def solve(self, index, total, subset, nums, target, result):
        if total == target:
            result.append(subset.copy())
            return
        if total > target:
            return
        if index >= len(nums):
            return

        Sum = total + nums[index]
        subset.append(nums[index])
        self.solve(index, Sum, subset, nums, target, result)

        Sum = total
        subset.pop()
        self.solve(index+1, Sum, subset, nums, target, result)

# Example usage:
if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7
    sol = Solution()
    combinations = sol.combinationSum(candidates, target)
    print(combinations)

        