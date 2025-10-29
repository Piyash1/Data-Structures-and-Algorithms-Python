class Solution:
    def isLeapYear(self, year):
        """
        :type year: int
        :rtype: bool
        """
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
        
# Example usage:
if __name__ == "__main__":
    year = int(input("Enter a year: "))
    solution = Solution()
    if solution.isLeapYear(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
        