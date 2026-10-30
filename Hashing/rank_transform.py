# 1331. Rank Transform of an Array

from typing import List

class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        sorted_array = sorted(arr)

        rank = {}

        current_rank = 1

        for num in sorted_array:
            if num not in rank:
                rank[num] = current_rank
                current_rank += 1
        
        result = []

        for num in arr:
            result.append(rank[num])
        
        return result


# Example usage
if __name__ == "__main__":
    solution = Solution()
    arr = [40,10,20,30]
    print(solution.arrayRankTransform(arr))
