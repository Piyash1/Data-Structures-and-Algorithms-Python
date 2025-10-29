# Find the Frequency

class Solution:
    def findFrequency(self, arr, x):
        frequency_dict = {}
        
        for num in arr:
            frequency_dict[num] = frequency_dict.get(num, 0) + 1
            
        return frequency_dict.get(x, 0)
    
ob = Solution()
arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
x = 3
print(ob.findFrequency(arr, x))
    