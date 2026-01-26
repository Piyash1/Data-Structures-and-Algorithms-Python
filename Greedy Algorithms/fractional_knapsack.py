# Given two arrays, val[] and wt[] , representing the values and weights of items, and an integer capacity representing the maximum weight a knapsack can hold, determine the maximum total value that can be achieved by putting items in the knapsack. You are allowed to break items into fractions if necessary.
# Return the maximum value as a double, rounded to 6 decimal places.

class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        items = []
        
        # store value, weight and value/weight ratio for each item
        for i in range(len(val)):
            items.append((val[i], wt[i], val[i] / wt[i]))
            
        # sort items by value/weight ratio in descending order
        items.sort(key=lambda x: x[2], reverse=True)
        
        total_value = 0.0
        
        for value, weight, ratio in items:
            if capacity >= weight:
                capacity -= weight
                total_value += value
            else:
                total_value += ratio * capacity
                break
        return round(total_value, 6)
    
sol = Solution()
val = [60, 100, 120]
wt = [10, 20, 30]
capacity = 50
print(sol.fractionalKnapsack(val, wt, capacity))  # Output: 240.0