# Leetcode no.20 - Valid Parentheses

class Solution:
    def is_valid(self, s):
        stack = []
        for bracket in s:
            if bracket == "(" or bracket == "{" or bracket == "[":
                stack.append(bracket)
            else:
                if len(bracket) == 0:
                    return False
                e = stack.pop()
                if((bracket == ")" and e == "(") or (bracket == "}" and e == "{") or (bracket == "]" and e == "[")):
                    continue
                else:
                    return False
        return len(stack) == 0

# Example usage
if __name__ == "__main__":
    sol = Solution()
    s = "()[]{}"
    print(sol.is_valid(s))