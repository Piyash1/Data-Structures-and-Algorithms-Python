# Given an array arr[], its starting position l and its ending position r. Sort the array using the merge sort algorithm.

class Solution:
    def mergeSort(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        left_sorted = self.mergeSort(left_half)
        right_sorted = self.mergeSort(right_half)
        return self.merge_array(left_sorted, right_sorted)

    # Merge two sorted arrays
    def merge_array(self, left, right):
        result = []
        i, j = 0, 0
        n, m = len(left), len(right)

        while i < n and j < m:
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        while i < n:
            result.append(left[i])
            i += 1
        while j < m:
            result.append(right[j])
            j += 1
        return result


# Example usage:
if __name__ == "__main__":
    sol = Solution()
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", arr)
    sorted_arr = sol.mergeSort(arr)
    print("Sorted array:", sorted_arr)
