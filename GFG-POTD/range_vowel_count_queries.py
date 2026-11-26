# https://www.geeksforgeeks.org/problems/range-vowel-count-queries-static/1

class Solution:
    def countVowels(self, s: str, queries: list[list[int]]) -> list[int]:
        # code here
        vowels = "aeiou"
        
        prefix = []
        count = 0
        
        # build prefix sum
        for ch in s:
            if ch in vowels:
                count += 1
            
            prefix.append(count)
            
        # answer queries
        result = []
        for l, r in queries:
            if l == 0:
                ans = prefix[r]
            else:
                ans = prefix[r] - prefix[l-1]
            
            result.append(ans)
            
        return result

# Example usage
if __name__ == "__main__":
    solution = Solution()
    s = "geeksforgeeks"
    queries = [[1, 3], [2, 4], [1, 9]]
    print(solution.countVowels(s, queries))
