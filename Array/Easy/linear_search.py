# Given an array, arr[] of n integers, and an integer element x, find whether element x is present in the array. Return the index of the first occurrence of x in the array, or -1 if it doesn't exist.

class Solution:
    def linearSearch(self, arr, x):
        n = len(arr)
        for i in range(n):
            if arr[i] == x:
                return i
        return -1

# Example usage:
solution = Solution()
arr = [2, 3, 4, 10, 40]
x = 40  
result = solution.linearSearch(arr, x)
print(result)