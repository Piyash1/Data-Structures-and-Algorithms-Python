# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]]

class Solution:
    def fourSum(self, nums, target):
        n = len(nums)
        ans = []
        nums.sort()  # Step 1: sort to simplify duplicates

        # 🚶‍♂️ Step 2: pick first two numbers
        for i in range(0, n):
            if i > 0 and nums[i] == nums[i - 1]:  # skip duplicates for i
                continue

            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:  # skip duplicates for j
                    continue

                # Step 3: two-pointer search for remaining two
                k = j + 1               # left pointer
                l = n - 1               # right pointer

                while k < l:
                    total = nums[i] + nums[j] + nums[k] + nums[l]

                    if total == target:
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1

                        # skip duplicate values for k
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        # skip duplicate values for l
                        while l > k and nums[l] == nums[l + 1]:
                            l -= 1

                    elif total < target:
                        k += 1           # need a larger sum

                    else:
                        l -= 1           # need a smaller sum

        return ans

# Example usage:
if __name__ == "__main__":
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    solution = Solution()
    print(solution.fourSum(nums, target))


# # Brute Force Approach (O(n^4) time complexity)
# def fourSum(nums, target):
#   n = len(nums)
#   if n < 4:
#     return []
#   myset = set()
  
#   for i in range(n):
#     for j in range(i+1, n):
#       for k in range(j+1, n):
#         for l in range(k+1, n):
#           total = nums[i]+nums[j]+nums[k]+nums[l]
#           if total == target:
#             temp = [nums[i], nums[j], nums[k], nums[l]]
#             temp.sort()
#             myset.add(tuple(temp))
#   result = []
#   for ans in myset:
#     result.append(list(ans))
#   return result

# # Example usage:
# nums = [1,0,-1,0,-2,2]
# target = 0
# print(fourSum(nums, target))

# # Better Approach (O(n^3) time complexity)
# def fourSum(nums, target):
#   n = len(nums)
#   if n < 4:
#     return []
#   myset = set()
  
#   for i in range(n):
#     for j in range(i+1, n):
#       hash_set = set()
#       for k in range(j+1, n):
#         fourth = target - (nums[i]+nums[j]+nums[k])
#         if fourth in hash_set:
#           temp = [nums[i], nums[j], nums[k], fourth]
#           temp.sort()
#           myset.add(tuple(temp))
#         hash_set.add(nums[k])
#   result = []
#   for ans in myset:
#     result.append(list(ans))
#   return result

# # Example usage:
# nums = [1,0,-1,0,-2,2]
# target = 0
# print(fourSum(nums, target))