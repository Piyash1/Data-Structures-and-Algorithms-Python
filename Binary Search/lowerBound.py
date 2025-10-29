# Given a sorted array arr[] and an integer x, find the index (0-based) of the largest element in arr[] that is less than or equal to x. This element is called the floor of x. If such an element does not exist, return -1.

class Solution:
    def floor(self, arr: list[int], x: int) -> int:
        low, high = 0, len(arr) - 1
        floor_index = -1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if arr[mid] == x:
                return mid
            elif arr[mid] <= x:
                floor_index = mid  # Update floor index
                low = mid + 1
            else:
                high = mid - 1
                
        return floor_index

# Example usage:
if __name__ == "__main__":
    arr = [1, 2, 8, 10, 10, 12, 19]
    x = 2
    sol = Solution()
    result = sol.floor(arr, x)
    print(f"Floor of {x} in arr: {result}")