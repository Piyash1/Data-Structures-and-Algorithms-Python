# 1539. Kth Missing Positive Number

from ast import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            missing = arr[mid] - (mid + 1)

            if missing < k:
                left = mid + 1
            else:
                right = mid - 1
        
        return left + k


# Example usage:
if __name__ == "__main__":
    solution = Solution()
    arr = [2, 3, 4, 7, 11]
    k = 5
    result = solution.findKthPositive(arr, k)
    print(result)  # Output: 9