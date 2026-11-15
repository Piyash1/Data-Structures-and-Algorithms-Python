# 1524. Number of Sub-arrays With Odd Sum

class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7

        even = 1
        odd = 0

        prefix = 0
        count = 0

        for num in arr:
            prefix += num

            if prefix % 2 == 1:
                count += even
                odd += 1
            else:
                count += odd
                even += 1
        
        return count % MOD

# Example usage
if __name__ == "__main__":
    solution = Solution()
    arr = [1, 3, 5]
    print(solution.numOfSubarrays(arr))
