# Leetcode no.1021 - Remove Outermost Parentheses

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        count = 0
        
        for ch in s:
            if ch == '(':
                count += 1
                if count > 1:
                    result.append(ch)
            else:
                count -= 1
                if count > 0:
                    result.append(ch)
        return ''.join(result)

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    test_str = "(()())(())(()(()))"
    print(sol.removeOuterParentheses(test_str))
        