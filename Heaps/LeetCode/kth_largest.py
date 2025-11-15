#Leetcode no.215 - Kth Largest Element in an Array
import random

class Solution(object):
    def findKthLargest(self, nums, k):
        left = 0
        right = len(nums) - 1
        
        while True:
            pivot_index = random.randint(left, right)
            pivot_index = self.partition(nums, left, right, pivot_index)
            if pivot_index == k - 1:
                return nums[pivot_index]
            elif pivot_index < k - 1:
                left = pivot_index + 1
            else:
                right = pivot_index - 1
    
    def partition(self, nums, left, right, pivot_index):
        pivot = nums[pivot_index]
        nums[left], nums[pivot_index] = nums[pivot_index], nums[left]
        index = left + 1
        for i in range(left + 1, right + 1):
            if nums[i] > pivot:
                nums[index], nums[i] = nums[i], nums[index]
                index += 1
        nums[left], nums[index - 1] = nums[index - 1], nums[left]
        return index - 1

# Example usage
if __name__ == "__main__":
    sol = Solution()
    arr = [3, 2, 1, 5, 6, 4]
    k = 2
    print(f"The kth({k}) largest element is:", sol.findKthLargest(arr, k))