# 14. Longest Common Prefix

from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        base = strs[0]
        result = ""
        
        for i in range(len(base)):
            for word in strs[1:]:
                if i == len(word) or word[i] != base[i]:
                    return result 
            result += base[i]
        return result

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    test_strs = ["flower","flow","flight"]
    print(sol.longestCommonPrefix(test_strs))