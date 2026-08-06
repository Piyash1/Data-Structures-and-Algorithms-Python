#3345. Smallest Divisible Digit Product I

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            product = 1
            for digit in str(n):
                product *= int(digit)
            if product % t == 0:
                return n
            n += 1

if __name__ == "__main__":
    solution = Solution()
    n = 10
    t = 2
    result = solution.smallestNumber(n, t)
    print(result)  # Output: 10