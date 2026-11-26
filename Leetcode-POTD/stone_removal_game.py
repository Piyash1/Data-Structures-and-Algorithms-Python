# 3360. Stone Removal Game

class Solution:
    def canAliceWin(self, n: int) -> bool:
        remove = 10
        alice_turn = True

        while n >= remove:
            n -= remove
            remove -= 1
            alice_turn = not alice_turn
        
        return not alice_turn


# Example usage
if __name__ == "__main__":
    solution = Solution()
    n = 12
    print(solution.canAliceWin(n))
