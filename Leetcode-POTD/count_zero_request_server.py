# 2747. Count Zero Request Servers

from typing import List

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # Sort logs by request time
        logs.sort(key=lambda log: log[1])

        # Keep original query positions
        sorted_queries = []

        for i in range(len(queries)):
            sorted_queries.append([queries[i], i])

        sorted_queries.sort()

        # Store answers
        result = [0] * len(queries)

        # Count requests from each server
        active = {}

        left = 0
        right = 0

        for query, index in sorted_queries:

            start = query - x

            # Add requests that are inside the right boundary
            while right < len(logs) and logs[right][1] <= query:

                server = logs[right][0]

                if server in active:
                    active[server] += 1
                else:
                    active[server] = 1

                right += 1

            # Remove requests that are outside the left boundary
            while left < len(logs) and logs[left][1] < start:

                server = logs[left][0]

                active[server] -= 1

                if active[server] == 0:
                    del active[server]

                left += 1

            # Count servers with zero requests
            result[index] = n - len(active)

        return result


# Example usage
if __name__ == "__main__":
    solution = Solution()
    n = 3
    logs = [[1,3],[2,6],[1,5]]
    x = 5
    queries = [10,11]
    print(solution.countServers(n, logs, x, queries))
