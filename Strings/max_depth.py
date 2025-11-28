# Leetcode no.1614 - Maximum Nesting Depth of the Parentheses

class Solution:
    def maxDepth(self, s: str) -> int:
        max_count = 0
        curr_count = 0

        for bracket in s:
            if bracket == "(":
                curr_count += 1
                max_count = max(max_count, curr_count)
            elif bracket == ")":
                curr_count -= 1
        return max_count

sol = Solution()
s = "(1+(2*3)+((8)/4))+1"
print(sol.maxDepth(s))