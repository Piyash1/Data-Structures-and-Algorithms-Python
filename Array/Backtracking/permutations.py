# 46. Permutations

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        path = []
        used = [False] * len(nums)

        def backtrack():
            # base case
            if len(path) == len(nums):
                result.append(path.copy())
                return

            # try every number
            for i in range(len(nums)):
                if used[i]:
                    continue
                
                # choose number
                path.append(nums[i])
                used[i] = True

                # explore
                backtrack()

                # undo
                path.pop()
                used[i] = False
                

        backtrack()
        return result

# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3]
    print(solution.permute(nums))
