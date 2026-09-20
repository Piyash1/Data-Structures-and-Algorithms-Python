# 3498. Reverse Degree of a String

class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0

        for i in range(len(s)):
            char = s[i]

            reverse_position = ord("z") - ord(char) + 1
            string_position = i + 1

            product = reverse_position * string_position
            total += product
        
        return total

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    input_string = "abc"
    result = solution.reverseDegree(input_string)
    print(f"The reverse degree of the string '{input_string}' is: {result}")
