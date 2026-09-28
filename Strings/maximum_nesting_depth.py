# 1111. Maximum Nesting Depth of Two Valid Parentheses Strings

class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        result = []
        depth = 0

        for char in seq:
            if char == "(":
                depth += 1
                result.append(depth % 2)
            else:
                result.append(depth % 2)
                depth -= 1
        
        return result




# Example usage
if __name__ == "__main__":
    solution = Solution()
    seq = "(()())"
    print(solution.maxDepthAfterSplit(seq))
