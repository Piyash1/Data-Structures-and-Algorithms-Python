# 3875. Construct Uniform Parity Array I

class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return True
    # Even - Even = Even
    # Odd - Odd = Even
    # Even - Odd = Odd
    # Odd - Even = Odd

# example usage
if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 2, 3, 4]
    print(solution.uniformArray(nums1))  # Output: True