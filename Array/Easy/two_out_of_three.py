# 2032. Two Out of Three

from typing import List


class Solution:
    def twoOutOfThree(
        self,
        nums1: List[int],
        nums2: List[int],
        nums3: List[int]
    ) -> List[int]:

        set1 = set(nums1)
        set2 = set(nums2)
        set3 = set(nums3)

        result = []

        all_numbers = set1 | set2 | set3

        for num in all_numbers:
            count = 0

            if num in set1:
                count += 1

            if num in set2:
                count += 1

            if num in set3:
                count += 1

            if count >= 2:
                result.append(num)

        return result


# Example usage
if __name__ == "__main__":
    solution = Solution()

    nums1 = [1, 1, 3, 2]
    nums2 = [2, 3]
    nums3 = [3]

    print(solution.twoOutOfThree(nums1, nums2, nums3))  # Answer: [2, 3]