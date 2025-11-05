# Leetcode no.1004 - Max Consecutive Ones III

class Solution(object):
    def longestOnes(self, nums, k):
        n = len(nums)
        maximum = 0
        left = 0
        right = 0
        zeroes = 0
        
        while right < n:
            if nums[right] == 0:
                zeroes += 1
            if zeroes > k:
                if nums[left] == 0:
                    zeroes -= 1
                left += 1
            if zeroes <= k:
                maximum = max(maximum, right-left+1)
            right += 1
        return maximum

# Example usage
if __name__ == "__main__":
    sol = Solution()
    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2
    result = sol.longestOnes(nums, k)
    print(result)
    
    # # Brute
    # def longestOnes(self, nums, k):
    #     n = len(nums)
    #     maximum = 0
        
    #     for i in range(n):
    #         zeroes = 0
    #         for j in range(i, n):
    #             if nums[j] == 0:
    #                 zeroes += 1
    #             if zeroes > k:
    #                 break
    #             maximum = max(maximum, j-i+1)
    #     return maximum