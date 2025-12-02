# Leetcode no.787 - Cheapest Flights Within K Stops

from typing import List
import sys
from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = [[] for _ in range(n)]
        for u, v, cost in flights:
            adj_list[u].append([v, cost])
        
        min_cost = [sys.maxsize for _ in range(n)]
        min_cost[src] = 0

        queue = deque() 
        queue.append([0, src, 0]) #step, node, cost
        while queue:
            step, node, cost = queue.popleft()
            for adj_node, price in adj_list[node]:
                new_price = cost + price
                if new_price < min_cost[adj_node]:
                    new_step = step+    1
                    if new_step == k+1:
                        if adj_node != dst:
                            continue
                    min_cost[adj_node] = new_price
                    queue.append([new_step, adj_node, new_price])
        
        if min_cost[dst] == sys.maxsize:
            return -1
        return min_cost[dst]
    
sol = Solution()
n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1
print(sol.findCheapestPrice(n, flights, src, dst, k))