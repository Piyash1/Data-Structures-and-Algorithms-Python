# 1614. Maximum Nesting Depth of the Parentheses

class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        max_depth = 0

        for char in s:
            if char == "(":
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == ")":
                depth -= 1
        
        return max_depth


# Example usage
if __name__ == "__main__":
    solution = Solution()
    s = "(1+(2*3)+((8)/4))+1"
    print(solution.maxDepth(s))
