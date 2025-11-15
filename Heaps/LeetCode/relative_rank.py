# Leetcode no.506 - Relative Ranks

import heapq

class Solution(object):
    def findRelativeRanks(self, score):
        n = len(score)
        result = [""] * n
        max_heap = []

        # push (-score, index) to simulate max-heap
        for i, s in enumerate(score):
            heapq.heappush(max_heap, (-s, i))
        
        rank = 1
        while max_heap:
            _, index = heapq.heappop(max_heap)

            if rank == 1:
                result[index] = "Gold Medal"
            elif rank == 2:
                result[index] = "Silver Medal"
            elif rank == 3:
                result[index] = "Bronze Medal"
            else:
                result[index] = str(rank)

            rank += 1

        return result

# Example usage
if __name__ == "__main__":
    sol = Solution()
    scores = [10, 3, 8, 9, 4]

    print(sol.findRelativeRanks(scores))
