# Leetcode no.22 - Generate Parentheses

from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        brackets = [""] * (2 * n)
        result = []
        self.solve(0, 0, brackets, result)
        return result
    
    def solve(self, index, total, brackets, result):
        if index >= len(brackets):
            if total == 0:
                result.append("".join(brackets))
            return
        if total > len(brackets) // 2:
            return
        elif total < 0:
            return
        
        # choice to put '('
        brackets[index] = '('
        self.solve(index + 1, total + 1, brackets, result)
        
        # choice to put ')'
        brackets[index] = ')'
        self.solve(index + 1, total - 1, brackets, result)


# Example usage:
if __name__ == "__main__":
    n = 3
    sol = Solution()
    parentheses = sol.generateParenthesis(n)
    print(parentheses)
        