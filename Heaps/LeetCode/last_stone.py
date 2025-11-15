# Leetcode no.104 - Last Stone Weight

import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            
            if first != second:
                new_stone = first - second
                heapq.heappush(stones, new_stone)
        if len(stones) == 1:
            return -heapq.heappop(stones)
        else:
            return 0

# Example usage
if __name__ == "__main__":
    sol = Solution()
    stones = [2,7,4,1,8,1]
    print("The weight of the last remaining stone is:", sol.lastStoneWeight(stones))            