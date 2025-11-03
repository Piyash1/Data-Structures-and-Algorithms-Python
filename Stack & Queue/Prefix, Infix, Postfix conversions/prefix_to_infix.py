class Solution:
    def prefix_to_infix(self, s):
        stack = []
        for char in s[::-1]:
            if char.isalnum():
                stack.append(char)
            else:
                # pop two operands
                operand1 = stack.pop()
                operand2 = stack.pop()
                
                # combine operands with operator
                new_expr = f"({operand1}{char}{operand2})"
                stack.append(new_expr)
        return stack[-1]

# Example usage
if __name__ == "__main__":
    sol = Solution()
    s = "/*a+bcd"
    print(sol.prefix_to_infix(s))