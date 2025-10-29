# Print Fibonacci of a number using Recursion

class Solution:
    def fibonacci(self, n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)
        
# Example Usage
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    ob = Solution()
    result = ob.fibonacci(n)
    print(f"The {n}th Fibonacci number is: {result}")