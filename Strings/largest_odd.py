# Leetcode no.1903 - Largest Odd Number in String

class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        for i in range(n - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[:i + 1]
        return ""

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    test_str = "35427"
    print(sol.largestOddNumber(test_str))  # Output: "35427"
    
    test_str2 = "4206"
    print(sol.largestOddNumber(test_str2))  # Output: ""