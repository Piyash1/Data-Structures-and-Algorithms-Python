class Solution:
    def precedence(self, ch):
        if ch == "+" or ch == "-":
            return 1
        if ch == "*" or ch == "/":
            return 2
        if ch == "^":
            return 3
        return 0
    
    def infix_to_prefix(self, s):
        s = s[::-1]
        s = s.replace("(", "temp").replace(")", "(").replace("temp", ")")
        stack = []
        result = []
        
        for char in s:
            if char.isalnum():
                result.append(char)
            elif char == "(":
                stack.append(char)
            elif char == ")":
                while stack and stack[-1] != "(":
                    result.append(stack.pop())
                stack.pop()
            else:
                while stack and self.precedence(stack[-1]) > self.precedence(char):
                    result.append(stack.pop())
                stack.append(char)
        
        while stack:
            result.append(stack.pop())
            
        return "".join(result[::-1])

# Example usage
if __name__ == "__main__":
    sol = Solution()
    s = "a*(b+c)/d"
    print(sol.infix_to_prefix(s))
                
            