class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()

        for char in s:
            if char in seen:
                return char
            else:
                seen.add(char)

sol = Solution()
s = "abccbaacz"
print(sol.repeatedCharacter(s))