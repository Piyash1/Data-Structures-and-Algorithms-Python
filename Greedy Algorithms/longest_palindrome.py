# 409. Longest Palindrome

class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}

        for char in s:
            freq[char] = freq.get(char, 0) + 1

        length = 0
        hasOdd = False

        for count in freq.values():
            length += (count // 2) * 2

            if count % 2 == 1:
                hasOdd = True

        if hasOdd:
            length += 1
        
        return length


# Example usage
if __name__ == "__main__":
    solution = Solution()
    s = "abccccdd"
    print(solution.longestPalindrome(s))
