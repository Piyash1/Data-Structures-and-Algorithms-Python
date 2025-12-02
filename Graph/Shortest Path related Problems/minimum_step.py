from typing import List
import sys
from collections import deque
 
class Solution:
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        distance = [sys.maxsize for _ in range(0, 100000)]
        distance[start] = 0
        
        queue = deque()
        queue.append([0, start]) # step, node
        while queue:
            step, num = queue.popleft()
            if num == end:
                return step
            for m in arr:
                new_num = (num * m) % 100000
                new_step = step + 1
                if new_step < distance[new_num]:
                    distance[new_num] = new_step
                    queue.append([new_step, new_num])
        return -1



sol = Solution()
arr = {2, 5, 7}
start = 3
end = 30
print(sol.minimumMultiplications(arr, start, end))