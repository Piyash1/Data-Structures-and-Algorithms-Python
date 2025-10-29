# def reverse(n):
#     """Reverse the digits of a non-negative integer n."""
#     if n < 0:
#         raise ValueError("Input must be a non-negative integer.")
#     reversed_num = 0
#     while n > 0:
#         digit = n % 10
#         reversed_num = reversed_num * 10 + digit
#         n //= 10
#     return reversed_num

# n = int(input("Enter a non-negative integer: "))
# print(f"The reverse of the number is {reverse(n)}.")

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        x *= sign
        reversed_num = 0
        while x:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10
        reversed_num *= sign
        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
        return reversed_num
    
# Example usage:
if __name__ == "__main__":
    number = int(input("Enter an integer: "))
    solution = Solution()
    print(f"The reverse of the number is {solution.reverse(number)}.")