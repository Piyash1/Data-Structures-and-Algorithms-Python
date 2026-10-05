# 856. Score of Parentheses

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for char in s:
            if char == '(':
                stack.append(0)

            else:  # char == ')'
                current_score = stack.pop()

                if current_score == 0:
                    score = 1
                else:
                    score = 2 * current_score

                stack[-1] += score

        return stack[0]


# Example usage
if __name__ == "__main__":
    solution = Solution()

    s = "(()())"

    print(solution.scoreOfParentheses(s))