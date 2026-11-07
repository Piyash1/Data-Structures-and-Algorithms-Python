# 1882. Process Tasks Using Servers

import heapq
class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        available = []
        busy = []

        result = []

        # Step 1: Put all servers into available heap
        for i in range(len(servers)):
            heapq.heappush(available, (servers[i], i))

        time = 0

        # Step 2: Process tasks one by one
        for i in range(len(tasks)):

            # Task i arrives at time i
            time = max(time, i)

            # Step 3: Release servers that finished their tasks
            while busy and busy[0][0] <= time:

                finish, weight, index = heapq.heappop(busy)

                heapq.heappush(available, (weight, index))

            # Step 4: If no server is free, wait
            if len(available) == 0:

                time = busy[0][0]

                while busy and busy[0][0] <= time:

                    finish, weight, index = heapq.heappop(busy)

                    heapq.heappush(available, (weight, index))

            # Step 5: Choose the best available server
            weight, index = heapq.heappop(available)

            result.append(index)

            # Step 6: Calculate when the server will finish
            finish = time + tasks[i]

            heapq.heappush(busy, (finish, weight, index))

        return result


# Example usage
if __name__ == "__main__":
    solution = Solution()
    servers = [3,3,2]
    tasks = [1,2,3,2,1,2]
    print(solution.assignTasks(servers, tasks))

