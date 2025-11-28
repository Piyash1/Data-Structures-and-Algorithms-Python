# Leetcode no. 242 Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_freq = {}
        for char in s:
            char_freq[char] = char_freq.get(char, 0)+1
        
        for char in t:
            if char not in char_freq:
                return False
            else:
                if char_freq[char] == 0:
                    return False
                else:
                    char_freq[char] -= 1
        return True

# Example usage
if __name__ == "__main__":
    sol = Solution()
    s = "anagram"
    t = "nagaram"
    print(sol.isAnagram(s, t))