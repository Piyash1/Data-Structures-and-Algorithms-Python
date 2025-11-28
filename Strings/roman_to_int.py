# Leetcode no.13 - Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        result = 0
        d = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

        for i in range(0, n):
            if i < n-1 and d[s[i]] < d[s[i+1]]:
                result -= d[s[i]]
            else:
                result += d[s[i]]
        return result

sol = Solution()
s = "MCMXCIV"
print(sol.romanToInt(s))