# Find the largest element of a given array

class Solution:
    def largest_element(self, arr):
        n = len(arr)
        largest = arr[0]
        for i in range(n):
            if  arr[i] > largest:
                largest = arr[i]    
        return largest
        
# Example usage
solution = Solution()
arr = [10, 20, 30, 25, 15, 50, 35]
result = solution.largest_element(arr)
print(result)

