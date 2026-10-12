#4065. Rearrange Array by Removing Distinct Values

from collections import Counter

class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        freq = Counter(nums)
        result = []

        while freq:
            values = sorted(freq.keys())

            for num in values:
                result.append(num)
                freq[num] -= 1
                if freq[num] == 0:
                    del freq[num]
        return result


# Example usage:
if __name__ == "__main__":
    solution = Solution()
    nums = [4, 3, 2, 4, 1, 3]
    rearranged_array = solution.rearrangeArray(nums)
    print(rearranged_array)