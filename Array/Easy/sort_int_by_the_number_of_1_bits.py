# 1356. Sort Integers by The Number of 1 Bits

class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        def count_bits(num):
            binary = bin(num)
            ones = binary.count("1")
            return ones
        
        arr.sort(key = lambda num: (count_bits(num), num))
        return arr

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    sorted_arr = solution.sortByBits(arr)
    print(sorted_arr)  # Output: [0, 1, 2, 4, 8, 3, 5, 6, 7]