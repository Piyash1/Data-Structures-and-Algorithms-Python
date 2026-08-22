# 3622. Check Divisibility by Digit Sum and Product

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        original = n
        digit_sum = 0
        digit_product = 1

        while n > 0:
            digit = n % 10

            digit_sum += digit
            digit_product *= digit

            n //= 10
        
        total = digit_sum + digit_product

        return original % total == 0


# Example usage:
if __name__ == "__main__":
    solution = Solution()
    n = 99
    result = solution.checkDivisibility(n)
    print(f"Is {n} divisible by the sum and product of its digits? {result}")