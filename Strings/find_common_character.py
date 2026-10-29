# 1002. Find Common Characters

from collections import Counter
from typing import List

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        common = Counter(words[0])

        for word in words[1:]:
            current = Counter(word)
            common &= current

        result = []

        for char in common:
            count = common[char]

            for i in range(count):
                result.append(char)

        return result        


# Example usage
if __name__ == "__main__":
    solution = Solution()
    words = ["bella","label","roller"]
    print(solution.commonChars(words))
