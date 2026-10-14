# 3723. Maximize Sum of Squares of Digits

class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > (9*num):
            return ""

        result = []
        for i in range(num):
            digit = min(9, sum)
            result.append(str(digit))
            sum -= digit

        return "".join(result)


# Exmaple usage
if __name__ == "__main__":
    solution = Solution()
    num = 2
    sum = 3
    print(solution.maxSumOfSquares(num, sum))
