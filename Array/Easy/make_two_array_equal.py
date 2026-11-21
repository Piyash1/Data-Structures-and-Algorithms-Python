# 1460. Make Two Arrays Equal by Reversing Subarrays

class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        target.sort()
        arr.sort()

        return target == arr

# Example usage
if __name__ == "__main__":
    solution = Solution()
    target = [1, 2, 3, 4]
    arr = [2, 4, 1, 3]
    print(solution.canBeEqual(target, arr))
