# Leetcode no.796 - Rotate String

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        combined = s + s
        if goal in combined:
            return True
        return False

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    s = "abcde"
    goal = "cdeab"
    print(sol.rotateString(s, goal))  # Output: True
    
    s2 = "abcde"
    goal2 = "abced"
    print(sol.rotateString(s2, goal2))  # Output: False


# # Brute Force Approach
# def rotateString(self, s: str, goal: str) -> bool:
#         if len(s) != len(goal):
#             return False
        
#         curr_str = s
#         for _ in range(len(s)):
#             if curr_str == goal:
#                 return True
#             curr_str = curr_str[-1] + curr_str[:-1]
#         return False