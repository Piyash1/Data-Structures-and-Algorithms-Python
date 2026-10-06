# 921. Minimum Add to Make Parentheses Valid

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        additions = 0
        open = 0

        for char in s:
            if char == '(':
                open += 1

            else:  # char == ')'
                if open > 0:
                    open -= 1
                else:
                    additions += 1

        return additions + open


# Example usage
if __name__ == "__main__":
    solution = Solution()

    s = "()))(("

    print(solution.minAddToMakeValid(s))