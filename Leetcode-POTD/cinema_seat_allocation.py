# 1386. Cinema Seat Allocation

from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved = {}

        for row, seat in reservedSeats:
            if not row in reserved:
                reserved[row] = set()
            reserved[row].add(seat)
        
        ans = (n - len(reserved)) * 2

        for seats in reserved.values():
            left = 2 not in seats and 3 not in seats and 4 not in seats and 5 not in seats
            middle = 4 not in seats and 5 not in seats and 6 not in seats and 7 not in seats
            right = 6 not in seats and 7 not in seats and 8 not in seats and 9 not in seats

            if left and right:
                ans += 2
            elif left or middle or right:
                ans += 1
        
        return ans


# Example usage:
if __name__ == "__main__":
    solution = Solution()
    n = 3
    reservedSeats = [[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]]
    print(solution.maxNumberOfFamilies(n, reservedSeats))  # Output: 4