# Leetcode no.735 - Asteroid Collision

class Solution(object):
    def asteroidCollision(self, asteroids):
        n = len(asteroids)
        stack = []
        
        for i in range(n):
            if asteroids[i] > 0:
                stack.append(asteroids[i])
            else:
                while len(stack) != 0 and stack[-1] > 0 and stack[-1] < abs(asteroids[i]):
                    stack.pop()
                if len(stack) != 0 and stack[-1] == abs(asteroids[i]):
                    stack.pop()
                elif len(stack) == 0 or stack[-1] < 0:
                    stack.append(asteroids[i])
        return stack

# Example usage
if __name__ == "__main__":
    sol = Solution()
    asteroids = [3,5,-6,2,-1,4]
    print(sol.asteroidCollision(asteroids))