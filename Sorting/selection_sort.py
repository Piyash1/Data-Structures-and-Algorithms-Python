# Given an array arr, use selection sort to sort arr[] in increasing order.

class Solution: 
    def selectionSort(self, arr):
        n = len(arr)
        for i in range(n):
            # Assume the minimum is the first element
            min_index = i
            # Iterate through the unsorted elements
            for j in range(i + 1, n):
                # Update min_index if a smaller element is found
                if arr[j] < arr[min_index]:
                    min_index = j
            # Swap the found minimum element with the first element of the unsorted part
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    arr = [64, 25, 12, 22, 11]
    sorted_arr = sol.selectionSort(arr)
    print("Sorted array:", sorted_arr)  
    
    

# Descending order

# def selectionSort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_index = i  # Fixed: Consistent spelling
#         for j in range(i + 1, n):
#             if arr[j] > arr[min_index]:  # Now references the correct variable
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#     return arr

# arr = [64, 25, 12, 22, 11]
# result = selectionSort(arr)
# print(result)  # Output: [11, 12, 22, 25, 64]