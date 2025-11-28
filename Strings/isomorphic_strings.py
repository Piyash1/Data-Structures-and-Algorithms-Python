# Leetcode no.205 - Isomorphic Strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mapping_s_t = {}
        mapping_t_s = {}
        
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            
            if char_s not in mapping_s_t:
                mapping_s_t[char_s] = char_t
            elif mapping_s_t[char_s] != char_t:
                return False
            
            if char_t not in mapping_t_s:
                mapping_t_s[char_t] = char_s
            elif mapping_t_s[char_t] != char_s:
                return False
        return True

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    s1 = "egg"
    t1 = "add"
    print(sol.isIsomorphic(s1, t1))  # Output: True
    
    s2 = "foo"
    t2 = "bar"
    print(sol.isIsomorphic(s2, t2))  # Output: False
    
    s3 = "paper"
    t3 = "title"
    print(sol.isIsomorphic(s3, t3))  # Output: True