# Leetcode no.151 - Reverse Words in a String
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        result = []
        
        for i in range(len(words) - 1, -1, -1):
            result.append(words[i])
            if i != 0:
                result.append(' ')
        return ''.join(result)

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    test_str = "  Hello World  "
    print(f"'{sol.reverseWords(test_str)}'")