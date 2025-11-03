class Solution:
    def nextLargerElement(self, arr):
        n = len(arr)
        result = [-1] * n
        stack = []
        
        for i in range(n-1, -1, -1):
            while len(stack) != 0 and stack[-1] <= arr[i]:
                stack.pop()
            if len(stack) != 0:
                result[i] = stack[-1]
            stack.append(arr[i])
        return result

# Example usage
if __name__ == "__main__":
    sol = Solution()
    arr = [1, 3, 2, 4]
    print(sol.nextLargerElement(arr))