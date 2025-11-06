# Leetcode no.904 - Fruit Into Baskets

class Solution(object):
    def totalFruit(self, fruits):
        n = len(fruits)
        maximum = 0
        my_dict = {}
        left = 0
        right = 0
        
        while right < n:
            my_dict[fruits[right]] = my_dict.get(fruits[right], 0)+1
            if len(my_dict) > 2:
                my_dict[fruits[left]] -= 1
                if my_dict[fruits[left]] == 0:
                    del my_dict[fruits[left]]
                left += 1
            if len(my_dict) <= 2:
                maximum = max(maximum, right-left+1)
            right += 1
        return maximum

# Example usage
if __name__ == "__main__":
    sol = Solution()
    fruits = [1,2,1]
    print(sol.totalFruit(fruits))
                    

# # Brute Force
# def totalFruit(self, fruits):
#         n = len(fruits)
#         maximum = 0
        
#         for i in range(n):
#             my_set = set()
#             for j in range(i, n):
#                 my_set.add(fruits[j])
#                 if len(my_set) > 2:
#                     break
#                 maximum = max(maximum, j-i+1)
#         return maximum