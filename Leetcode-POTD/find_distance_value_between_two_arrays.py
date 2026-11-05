# 1385. Find the Distance Value Between Two Arrays

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        count = 0

        def has_num_in_range(arr, left, right):
            low = 0
            high = len(arr)-1
            
            while low <= high:
                mid = (low+high) // 2
                value = arr[mid]

                if left <= value <= right:
                    return True
                
                elif value < left:
                    low = mid + 1
                
                else:
                    high = mid - 1

            return False

        for x in arr1:
            left = x - d
            right = x + d

            if not has_num_in_range(arr2, left, right):
                count += 1

        return count


# Example usage
if __name__ == "__main__":
    solution = Solution()
    arr1 = [4,5,8]
    arr2 = [10,9,1,8]
    d = 2
    print(solution.findTheDistanceValue(arr1, arr2, d))
