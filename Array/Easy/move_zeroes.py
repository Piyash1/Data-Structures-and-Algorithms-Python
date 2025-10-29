# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

class Solotion:
    def moveZeroes(self, nums):
        n = len(nums)
        if n == 1:
            return
        i = 0
        while i < n:
            if nums[i] == 0:
                break
            i += 1
        if i == n:
            return
        j = i + 1
        while j < n:
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        return nums

# Example usage:
nums = [0, 1, 0, 3, 12, 5, 0, 7]
solution = Solotion()
print(solution.moveZeroes(nums)) 


# # Brute Force Approach
# def move_zeroes(nums):
#     n = len(nums)
#     temp = []
#     for i in range(n):
#         if nums[i] != 0:
#             temp.append(nums[i])
#     nz = len(temp)
#     for i in range(0, nz):
#         nums[i] = temp[i]
#     for i in range(nz, n):
#         nums[i] = 0
#     return nums

# nums = [0, 1, 0, 3, 12]
# print(move_zeroes(nums))  


# step-1: loop through array until nums[i] = 0, if you find zero then break loop otherwise continue i +=1

# step-2: start another loop for j(i+1). if nums[j] is not zero then swap with nums[i]
# and i += 1
