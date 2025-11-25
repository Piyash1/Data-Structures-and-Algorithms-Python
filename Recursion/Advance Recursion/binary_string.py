class Solution:
    def binstr(self, n):
        numbers = ["0"] * n
        result = []
        self.backtrack(0, numbers, result)
        return result
    
    def backtrack(self, index, numbers, result):
        if index == len(numbers):
            result.append("".join(numbers))
            return
        
        # Put '0'
        numbers[index] = "0"
        self.backtrack(index + 1, numbers, result)
        
        # Put '1'
        numbers[index] = "1"
        self.backtrack(index + 1, numbers, result)


# Example usage:
if __name__ == "__main__":
    n = 3
    sol = Solution()
    binary_strings = sol.binstr(n)
    print(binary_strings)