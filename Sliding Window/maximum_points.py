# Leetcode no.1423 - Maximum Points You Can Obtain from Cards
class Solution(object):
    def maxScore(self, cardPoints, k):
        n = len(cardPoints)
        if n == k:
            return sum(cardPoints)
        left_sum = 0
        right_sum = 0
        for i in range(0, k):
            left_sum += cardPoints[i]
        maximum = left_sum
        right_index = n-1
        for i in range(k-1, -1, -1):
            left_sum -= cardPoints[i]
            right_sum += cardPoints[right_index]
            maximum = max(maximum, left_sum+right_sum)
            right_index -= 1
        return maximum
    
# Example usage
if __name__ == "__main__":
    sol = Solution()
    cardPoints = [1,2,3,4,5,6,1]
    k = 3
    result = sol.maxScore(cardPoints, k)
    print(result)
            