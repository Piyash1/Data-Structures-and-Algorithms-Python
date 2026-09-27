class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ")":
                temp = []
                while stack[-1] != "(":
                    temp.append(stack.pop())

                stack.pop()

                stack.extend(temp)

            else:
                stack.append(char)

        return "".join(stack)



#Example usage
if __name__ == "__main__":
    solution = Solution()
    s = "(u(love)i)"
    print(solution.reverseParentheses(s))