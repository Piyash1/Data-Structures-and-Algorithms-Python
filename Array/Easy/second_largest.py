# Find the second largest and second smallest element from the array.

from typing import List

class Solution:
    def getSecondOrderElements(self, n: int,  a: List[int]) -> List[int]:
        n = len(a)
        largest = second_largest = float('-inf')
        smallest = second_smallest = float('inf')
        for i in range(n):
            if a[i] > largest:
                second_largest = largest
                largest = a[i]
            elif a[i] > second_largest and a[i] != largest:
                second_largest = a[i]
                
            if a[i] < smallest:
                second_smallest = smallest
                smallest = a[i]
            elif a[i] < second_smallest and a[i] != smallest:
                second_smallest = a[i]
        return [second_largest, second_smallest]
    

# Example usage
solution = Solution()
a = [10, 20, 30, 25, 15, 50, 35]
n = len(a)
result = solution.getSecondOrderElements(n, a)
print(result)