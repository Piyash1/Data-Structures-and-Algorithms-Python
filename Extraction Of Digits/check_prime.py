class Solution:
    def isPrime(self, num):
        """Check if a number is prime."""
        if num <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

n = int(input("Enter a positive integer: "))
solution = Solution()
if solution.isPrime(n):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")    