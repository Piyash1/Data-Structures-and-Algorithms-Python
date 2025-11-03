class Solution:
    def postfix_to_prefix(self, s):
        stack = []
        for char in s:
            if char.isalnum():
                stack.append(char)
            else:
                # pop two operands
                operand2 = stack.pop()
                operand1 = stack.pop()
                
                # combine operands with operator
                new_expr = f"{char}{operand1}{operand2}"
                stack.append(new_expr)
        return stack[-1]

# Example usage
if __name__ == "__main__":
    sol = Solution()
    s = "ABC/-AK/L-*"
    print(sol.postfix_to_prefix(s))