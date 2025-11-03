class Solution:
    def postfix_to_infix(self, s):
        stack = []
        for char in s:
            if char.isalnum():
                stack.append(char)
            else:
                # pop two operands
                operand2 = stack.pop()
                operand1 = stack.pop()
                
                # combine operands with operator
                new_expr = f"({operand1}{char}{operand2})"
                stack.append(new_expr)
        return stack[-1]

# Example usage
if __name__ == "__main__":
    sol = Solution()
    s = "abc+*d/"
    print(sol.postfix_to_infix(s))