# 1658. Minimum Operations to Reduce X to Zero

class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        target = sum(nums) - x

        if target < 0:
            return -1
        
        if target == 0:
            return n
        
        left = 0
        window_sum = 0
        max_len = -1

        for right in range(n):
            window_sum += nums[right]

            while window_sum > target:
                window_sum -= nums[left]
                left += 1
            
            if window_sum == target:
                max_len = max(max_len, right - left + 1)
        
        return -1 if max_len == -1 else n - max_len

# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums = [1,1,4,2,3]
    x = 5
    print(solution.minOperations(nums, x))
