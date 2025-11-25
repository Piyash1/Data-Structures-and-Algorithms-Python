# Leetcode no. 216: Combination Sum III

from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        self.backtrack(1, 0, [], result, n, k)
        return result
    
    def backtrack(self, last, total, subset, result, n, k):
        if total == n and len(subset) == k:
            result.append(subset.copy())
            return
        if total > n or len(subset) > k:
            return
        
        for i in range(last, 10):
            Sum = total + i
            subset.append(i)
            self.backtrack(i+1, Sum, subset, result, n, k)
            Sum = total
            subset.pop()

# Example usage:
if __name__ == "__main__":
    k = 3
    n = 7
    sol = Solution()
    combinations = sol.combinationSum3(k, n)
    print(combinations)