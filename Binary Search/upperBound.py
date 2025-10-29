# You are given a sorted array ‘arr’ containing ‘n’ integers and an integer ‘x’.Implement the ‘upper bound’ function to find the index of the upper bound of 'x' in the array.

class Solution:
    def upperBound(arr: list[int], x: int, n: int) -> int:
        ub = n
        n = len(arr)
        low = 0
        high = n-1
        while low <= high:
            mid = (low+high)// 2
            if arr[mid] > x:
                ub = mid
                high = mid - 1
            else:
                low = mid + 1
        return ub

# Example usage:
if __name__ == "__main__":
    arr = [1, 2, 4, 4, 5, 6]
    x = 5
    n = len(arr)
    result = Solution.upperBound(arr, x, n)
    print(f"The upper bound of {x} in the array is at index: {result}")