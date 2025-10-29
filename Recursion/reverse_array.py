# Print reverse of a given array using Recursion

class Solution:
    def reverseArray(self, arr, start, end):
        if start >= end:
            return
        arr[start], arr[end] = arr[end], arr[start]
        self.reverseArray(arr, start + 1, end - 1)
        
# Example Usage
if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements separated by space: ").split()))
    ob = Solution()
    ob.reverseArray(arr, 0, len(arr) - 1)
    print("Reversed array is:", arr)