# Leetcode no.3 - Longest Substring Without Repeating Characters

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        left = 0
        right = 0
        my_dict = {}
        maximum = 0
        
        while right < n:
            if s[right] in my_dict:
                left = max(left, my_dict[s[right]]+1)
            maximum = max(maximum, right-left+1)
            my_dict[s[right]] = right
            right += 1
        return maximum

# Example usage
if __name__ == "__main__":
    sol = Solution()
    s = "abcabcbb"
    print(sol.lengthOfLongestSubstring(s))