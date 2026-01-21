# Geek is going for a training program for n days. He can perform any of these activities: 
# Running, Fighting, and Learning Practice. Each activity has some point on each day. 
# As Geek wants to improve all his skills, he can't do the same activity on two consecutive days. 
# Given a 2D array arr[][] of size n where arr[i][0], arr[i][1], and arr[i][2] represent 
# the merit points for Running, Fighting, and Learning on the i-th day, determine the 
# maximum total merit points Geek can achieve.

# Space-Optimized Tabulation Approach


class Solution:
    def maxMeritPoints(self, arr):
        prev = [0] * 4
        n = len(arr)
        # Base case for day 0
        prev[0] = max(arr[0][1], arr[0][2])  # If last activity was Running
        prev[1] = max(arr[0][0], arr[0][2])  # If last activity was Fighting
        prev[2] = max(arr[0][0], arr[0][1])  # If last activity was Learning
        prev[3] = max(arr[0][0], arr[0][1], arr[0][2])  # If no activity was done
        
        for day in range(1, n):
            curr = [0] * 4
            for last_activity in range(4):
                max_points = 0
                for activity in range(3):
                    if activity != last_activity:
                        points = arr[day][activity] + prev[activity]
                        max_points = max(max_points, points)
                curr[last_activity] = max_points
            prev = curr
        return prev[3]  # Max points on last day with no restriction on last activity

# Test the solution
sol = Solution()
arr = [[1, 2, 5], [3, 1, 1], [3, 3, 3]]
print(sol.maxMeritPoints(arr))  # Output: 11

# Tabulation Approach
# class Solution:
#     def maxMeritPoints(self, arr):
#         n = len(arr)
#         dp = [[-1] * 4 for _ in range(n)]
        
#         # Base case for day 0
#         dp[0][0] = max(arr[0][1], arr[0][2])  # If last activity was Running
#         dp[0][1] = max(arr[0][0], arr[0][2])  # If last activity was Fighting
#         dp[0][2] = max(arr[0][0], arr[0][1])  # If last activity was Learning
#         dp[0][3] = max(arr[0][0], arr[0][1], arr[0][2])  # If no activity was done
        
#         for day in range(1, n):
#             for last_activity in range(4):
#                 max_points = 0
#                 for activity in range(3):
#                     if activity != last_activity:
#                         points = arr[day][activity] + dp[day - 1][activity]
#                         max_points = max(max_points, points)
#                 dp[day][last_activity] = max_points
       
#         return dp[n - 1][3]  # Max points on last day with no restriction on last activity 


# Memoization Approach
# class Solution:
#     def solve(self, day, last_activity, arr, dp):
#         if day == 0:
#             max_points = 0
#             for activity in range(3):
#                 if activity != last_activity:
#                     max_points = max(max_points, arr[day][activity])
#             return max_points
        
#         if dp[day][last_activity] != -1:
#             return dp[day][last_activity]
        
#         max_points = 0
#         for activity in range(3):
#             if activity != last_activity:
#                 points = arr[day][activity] + self.solve(day - 1, activity, arr, dp)
#                 max_points = max(max_points, points)
        
#         dp[day][last_activity] = max_points
#         return max_points
    
#     def maxMeritPoints(self, arr):
#         n = len(arr)
#         dp = [[-1] * 4 for _ in range(n)]
#         return self.solve(n - 1, 3, arr, dp)  # 3 means no activity chosen yet


# Brute Force Recursion Approach
# class Solution:
#     def solve(self, day, last_activity, arr):
#         if day == 0:
#             max_points = 0
#             for activity in range(3):
#                 if activity != last_activity:
#                     max_points = max(max_points, arr[day][activity])
#             return max_points
        
#         max_points = 0
#         for activity in range(3):
#             if activity != last_activity:
#                 points = arr[day][activity] + self.solve(day - 1, activity, arr)
#                 max_points = max(max_points, points)
        
#         return max_points
    
#     def maxMeritPoints(self, arr):
#         n = len(arr)
#         return self.solve(n - 1, 3, arr)  # 3 means no activity chosen yet