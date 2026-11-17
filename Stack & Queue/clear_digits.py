# 3174. Clear Digits

class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for char in s:
            if char.isdigit():
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)


# Example usage
if __name__ == "__main__":
    solution = Solution()
    s = "ab3c2"

    print(solution.clearDigits(s))