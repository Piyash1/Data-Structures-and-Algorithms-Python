# You're given a sorted array 'a' of 'n' integers and an integer 'x'.
# Find the floor and ceiling of 'x' in 'a[0..n-1]'.

class Solution:
    def getFloorAndCeil(a, n, x):
        floor = -1
        ceil = -1
        n = len(a)
        low = 0
        high = n-1
        while low <= high:
            mid = (low+high)//2
            if a[mid] == x:
                return [a[mid], a[mid]]
            elif a[mid] > x:
                ceil = a[mid]
                high = mid-1
            else:
                floor= a[mid]
                low = mid+1
        return [floor, ceil]
    
# Example usage:
if __name__ == "__main__":
    a = [1, 2, 8, 10, 10, 12, 19]
    x = 5
    n = len(a)
    result = Solution.getFloorAndCeil(a, n, x)
    print("Floor and Ceil of", x, "are:", result) 
