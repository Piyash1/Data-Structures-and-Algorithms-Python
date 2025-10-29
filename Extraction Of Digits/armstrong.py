class Solution(object):
    def isArmstrong(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 0:
            return False
        original = n
        digits = len(str(n))
        armstrong_sum = 0
        while n > 0:
            digit = n % 10
            armstrong_sum += digit ** digits
            n //= 10
        return original == armstrong_sum
    
# Example usage:
if __name__ == "__main__":  
    number = int(input("Enter a non-negative integer: "))
    solution = Solution()
    if solution.isArmstrong(number):
        print(f"{number} is an Armstrong number.")
    else:
        print(f"{number} is not an Armstrong number.")