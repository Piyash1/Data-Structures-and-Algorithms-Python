# Leetcode no 78: Subsets

class Solution(object):
    def subsets(self, nums):
        result = []
        self.solve(0, nums, [], result)
        return result
    
    def solve(self, index, nums, subset, result):
        if index == len(nums):
            result.append(subset.copy())
            return
        
        # Include
        subset.append(nums[index])
        self.solve(index + 1, nums, subset, result)

        # Exclude
        subset.pop()
        self.solve(index + 1, nums, subset, result)

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3]
    print(sol.subsets(nums)) 
