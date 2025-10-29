class Solution:
    def factors(self, n):
        """Return the factors of a positive integer n as a list."""
        if n <= 0:
            raise ValueError("Input must be a positive integer.")
        result = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                result.append(i)
                if i != n // i:
                    result.append(n // i)
        result.sort()
        return result

#Example usage:
if __name__ == "__main__":
    n = int(input("Enter a positive integer: "))
    solution = Solution()
    print(f"The factors of {n} are: {solution.factors(n)}.")
    
    

# # Alternative standalone function implementation to count factors:

# def factors_count(n):
#     """Return the number of factors of a positive integer n."""
#     if n <= 0:
#         raise ValueError("Input must be a positive integer.")
#     count = 0
#     for i in range(1, int(n**0.5) + 1):
#         if n % i == 0:
#             count += 1
#             if i != n // i:
#                 count += 1
#     return count

# n = int(input("Enter a positive integer: "))
# print(f"The number of factors of {n} is: {factors_count(n)}.")