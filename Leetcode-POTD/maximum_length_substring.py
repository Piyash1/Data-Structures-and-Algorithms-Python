# 3090. Maximum Length Substring With Two Occurrences

from typing import List
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq = {}
        left = 0
        ans = 0

        for right in range(len(s)):
            # Add s[right] to the frequency map
            freq[s[right]] = freq.get(s[right], 0) + 1

            # Window is invalid
            while freq[s[right]] > 2:
                freq[s[left]] -= 1
                left += 1

            # Window is valid, update the answer
            ans = max(ans, right - left + 1)

        return ans

# Example usage
if __name__ == "__main__":
    solution = Solution()
    s = "bcbbbcba"
    print(solution.maximumLengthSubstring(s))  # Output: 4