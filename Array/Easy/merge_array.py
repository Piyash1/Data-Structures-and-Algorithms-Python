# Given two sorted arrays a[] and b[], where each array may contain duplicate elements , the task is to return the elements in the union of the two arrays in sorted order.

class Solution:
    def findUnion(self, a, b):
        # code here 
        i, j = 0, 0
        n, m = len(a), len(b)
        result = []
        while i < n and j < m:
            if a[i] <= b[j]:
                if not result or result[-1] != a[i]:
                    result.append(a[i])
                i += 1
            else:
                if not result or result[-1] != b[j]:
                    result.append(b[j])
                j += 1
        while i < n:
            if not result or result[-1] != a[i]:
                result.append(a[i])
            i += 1
        while j < m:
            if not result or result[-1] != b[j]:  
                result.append(b[j])
            j += 1
        return result

# Example usage:
sol = Solution()
a = [1, 2, 2, 3, 4]
b = [2, 3, 5, 6]
print(sol.findUnion(a, b)) 