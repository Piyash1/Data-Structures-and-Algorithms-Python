# 2913. Subarrays Distinct Element Sum of Squares I

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0

        for i in range(n):
            seen = set()

            for j in range(i, n):
                seen.add(nums[j])
                count = len(seen)
                result += count * count

        return result


# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 1]
    print(solution.sumCounts(nums))
