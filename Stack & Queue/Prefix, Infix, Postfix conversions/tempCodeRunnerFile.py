else:
                while stack and self.precedence(stack[-1]) > self.precedence(char):
                    result.append(stack.pop())
                stack.append(char)