# Print factorial of a number using Recursion

class Solution:
    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n - 1)

# Example Usage
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    ob = Solution()
    result = ob.factorial(n)
    print(f"The factorial of {n} is: {result}")