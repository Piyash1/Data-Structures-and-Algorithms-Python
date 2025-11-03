class Solution:
    def preToPost(self, pre_exp):
        stack = []
        n = len(pre_exp)
        
        for i in range(n-1, -1, -1):
            char = pre_exp[i]
            
            if char.isalnum():
                stack.append(char)
            else:
                operand1 = stack.pop()
                operand2 = stack.pop()
            
                new_expr = operand1 + operand2 + char
                stack.append(new_expr)
            
        return stack[-1]

# Example usage
if __name__ == "__main__":
    sol = Solution()
    s = "*-A/BC-/AKL"
    print(sol.preToPost(s))