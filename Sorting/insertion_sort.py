# Given an array arr[] of positive integers.The task is to complete the insertsort() function which is used to implement Insertion Sort.

class Solution:
    def insertionSort(self, arr):
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            # Move elements of arr[0..i-1], that are greater than key,
            # to one position ahead of their current position
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
    
# Example usage:
if __name__ == "__main__":
    sol = Solution()
    arr = [12, 11, 13, 5, 6]
    print("Original array:", arr)
    sorted_arr = sol.insertionSort(arr)
    print("Sorted array:", sorted_arr)