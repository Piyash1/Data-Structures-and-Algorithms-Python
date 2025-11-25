def backtrack(index, subset, total):
    if total == k:
        result.append(subset.copy())
        return
    if total > k:
        return
    if index >= len(nums):
        return
    
    # choice to include nums[index]
    subset.append(nums[index])
    sum = total + nums[index]
    backtrack(index + 1, subset, sum)
    
    # choice to exclude nums[index]
    subset.pop()
    sum = total
    backtrack(index + 1, subset, sum)


result = []
nums = [1, 2, 3]
k = 3
backtrack(0, [], 0)
print(result)