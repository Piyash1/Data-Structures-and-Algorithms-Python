# Given an array, arr[]. Sort the array using bubble sort algorithm.

class Solution:
    def bubbleSort(self,arr):
        n = len(arr)
        for i in range(n-1):
            swapped = False
            for j in range(0, n-1-i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr


# Example usage:

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array is:", arr)
    solution = Solution()
    sorted_arr = solution.bubbleSort(arr)
    print("Sorted array is:", sorted_arr)

