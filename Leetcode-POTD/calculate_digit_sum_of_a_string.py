# 2243. Calculate Digit Sum of a String

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            result = ""

            for i in range(0, len(s), k):
                group = s[i:i + k]

                total = 0

                for digit in group:
                    total += int(digit)

                result += str(total)

            s = result

        return s


# Example usage
if __name__ == "__main__":
    solution = Solution()
    s = "11111222223"
    k = 3
    print(solution.digitSum(s, k))
