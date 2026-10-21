# 3863. Minimum Operations to Sort a String

class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        sorted_string = True

        # Step 1: Check if already sorted
        for i in range(n-1):
            if s[i] > s[i+1]:
                sorted_string = False
                break
        
        if sorted_string:
            return 0

        # Step 2: An unsorted string of length 2 is impossible
        if n == 2:
            return -1

        # Step 3: Find the smallest and largest characters
        mn = min(s)
        mx = max(s)

        # Step 4: Check if one operation is enough
        if s[0] == mn or s[n-1] == mx:
            return 1
        
        # Step 5: Check the middle characters
        for i in range(1, n-1):
            if s[i] == mn or s[i] == mx:
                return 2

        # Step 6: Otherwise, three operations are needed
        return 3


# Example usage
if __name__ == "__main__":
    solution = Solution()
    s = "card"
    print(solution.minOperations(s))
