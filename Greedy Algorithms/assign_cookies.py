# Leetcode Problem 455: Assign Cookies

from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = j = 0
        content_children = 0
        
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                content_children += 1
                i += 1
            j += 1
        return content_children
    
    
sol = Solution()
g = [1,2,3]
s = [1,1]
print(sol.findContentChildren(g, s))