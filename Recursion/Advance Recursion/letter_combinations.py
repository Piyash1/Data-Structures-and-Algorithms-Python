# Leetcode problem no. 17: Letter Combinations of a Phone Number

class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []
        
        phone_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        result = []
        
        def backtrack(index, current):
            if index == len(digits):
                result.append("".join(current))
                return
            
            possible_letters = phone_map[digits[index]]
            for letter in possible_letters:
                current.append(letter)
                backtrack(index + 1, current)
                current.pop()
        
        backtrack(0, [])
        return result

# Example usage:
if __name__ == "__main__":
    digits = "23"
    sol = Solution()
    combinations = sol.letterCombinations(digits)
    print(combinations)
