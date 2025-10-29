# Implement Quick Sort, a Divide and Conquer algorithm, to sort an array, arr[] in ascending order.
#Given an array arr[], with starting index low and ending index high, complete the functions partition() and quickSort().

class Solution:
    def quickSort(self, arr, low, high):
        if low < high:
            p_index = self.partition(arr, low, high)
            self.quickSort(arr, low, p_index - 1)
            self.quickSort(arr, p_index + 1, high)
    
    def partition(self, arr, low, high):
        pivot = arr[low]
        i = low
        j = high
        while i < j:
            while arr[i] <= pivot and i <= high-1:
                i += 1
            while arr[j] > pivot and j >= low+1:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[low], arr[j] = arr[j], arr[low]
        return j

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    print("Original array:", arr)
    sol.quickSort(arr, 0, n - 1)
    print("Sorted array:", arr)

