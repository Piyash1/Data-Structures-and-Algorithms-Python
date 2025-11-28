# Leetcode no.451 - Sort Characters By Frequency

class Solution:
    def frequencySort(self, s: str) -> str:
        result = ''
        hashmap ={}
        for char in s:
            hashmap[char] = hashmap.get(char, 0)+1
        
        sorted_char = sorted(hashmap.items(), key = lambda x: x[1], reverse = True)
        for char, freq in sorted_char:
            result = result + (char*freq)
        return result

sol = Solution()
s = "tree"
print(sol.frequencySort(s))