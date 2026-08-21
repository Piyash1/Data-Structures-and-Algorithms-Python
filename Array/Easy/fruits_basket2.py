# 3477. Fruits Into Baskets II

from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        used = [False] * n
        unplaced = 0

        for fruit in fruits:
            for j in range(n):
                if not used[j] and baskets[j] >=fruit:
                    used[j] = True
                    break

            else:
                unplaced += 1

        return unplaced


# Example usage:
if __name__ == "__main__":
    solution = Solution()
    fruits = [4, 2, 5]
    baskets = [3, 5, 4]
    result = solution.numOfUnplacedFruits(fruits, baskets)
    print(result)  # Output: 1