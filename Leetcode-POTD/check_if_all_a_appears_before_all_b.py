# 2124. Check if All A's Appears Before All B's

class Solution:
    def checkString(self, s: str) -> bool:
        seenb = False

        for char in s:
            if char == "b":
                seenb = True
                
            elif char == "a" and seenb:
                return False
        
        return True


# Example usage
if __name__ == "__main__":
    solution = Solution()
    s = "aaabbb"
    print(solution.checkString(s))
