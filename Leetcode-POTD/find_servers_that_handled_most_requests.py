# 1606. Find Servers That Handled Most Number of Requests

from sortedcontainers import SortedList
import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        free = SortedList(range(k))
        busy = []
        count = [0] * k

        for i in range(len(arrival)):
            start = arrival[i]
            duration = load[i]

            # Free servers that have finished by now
            while busy and busy[0][0] <= start:
                _, server = heapq.heappop(busy)
                free.add(server)          # ← fixed

            # No free server → drop the request
            if not free:
                continue
            
            # Find the best server
            preferred = i % k
            idx = free.bisect_left(preferred)

            if idx == len(free):
                server = free[0]
            else:
                server = free[idx]

            # Assign the request
            free.remove(server)
            count[server] += 1
            heapq.heappush(busy, (start + duration, server))
        
        max_count = max(count)
        return [i for i in range(k) if count[i] == max_count]


# Example usage
if __name__ == "__main__":
    solution = Solution()
    k = 3
    arrival = [1, 2, 3, 4, 5]
    load = [5, 2, 3, 3, 3]
    print(solution.busiestServers(k, arrival, load))
