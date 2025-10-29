# Print sum of first n terms using Recursion

class Solution:
    def sumOfN(self, n):
        if n == 0:
            return 0
        return n**3 + self.sumOfN(n - 1)
    
# Example Usage
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    ob = Solution()
    result = ob.sumOfN(n)
    print(f"The sum of first {n} natural numbers is: {result}")