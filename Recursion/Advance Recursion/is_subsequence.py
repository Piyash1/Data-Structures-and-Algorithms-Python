class Solution:
    def backtrack(self, subset, index, total):
        if total == K:
            # result.append(subset.copy())  # Uncomment if you want to collect the subset
            return True
        if index >= N:
            return False
        
        subset.append(arr[index])
        pick = self.backtrack(subset, index + 1, total + arr[index])
        if pick == True:
            return True
        
        e = subset.pop()
        # No need for Sum -= e; just pass total for not pick
        return self.backtrack(subset, index + 1, total)
    
    def checkSubsequenceSum(self, N, arr, K):
        return self.backtrack([], 0, 0)

# Example usage:
if __name__ == "__main__":
    N = 5
    arr = [1, 2, 3, 4, 5]
    K = 9
    sol = Solution()
    result = sol.checkSubsequenceSum(N, arr, K)
    print(result)  # Output: True or False