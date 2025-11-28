# Leetcode no.387 - First Unique Character in a String

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        for ch in s:
            hashmap[ch] = hashmap.get(ch, 0)+1

        for index, char in enumerate(s):
            if hashmap[char] == 1:
                return index
        return -1

sol =Solution()
s = "leetcode"
print(sol.firstUniqChar(s))