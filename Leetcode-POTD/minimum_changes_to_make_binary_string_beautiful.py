# 2914. Minimum Number of Changes to Make Binary String Beautiful

class Solution:
    def minChanges(self, s: str) -> int:
        changes = 0

        for i in range(0, len(s), 2):
            if s[i] != s[i+1]:
                changes += 1

        return changes


# Example usage
if __name__ == "__main__":
    solution = Solution()
    s = "1001"
    print(solution.minChanges(s))
