# Given arrival arr[] and departure dep[] times of trains on the same day, find the minimum number of platforms needed so that no train waits. A platform cannot serve two trains at the same time; if a train arrives before another departs, an extra platform is needed.

class Solution:    
    def minPlatform(self, arr, dep):
        arr.sort()
        dep.sort()
        i = 0 # Pointer for arrival
        j = 0 # Pointer for departure
        platform_needed = 0 
        max_platforms = 0
        
        while i < len(arr) and j < len(dep):
            if arr[i] <= dep[j]:
                platform_needed += 1
                max_platforms = max(max_platforms, platform_needed)
                i += 1
            else:
                platform_needed -= 1
                j += 1
        return max_platforms

sol = Solution()
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
print(sol.minPlatform(arr, dep))  # Output: 3