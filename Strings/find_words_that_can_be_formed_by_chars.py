# 1160. Find Words That Can Be Formed by Characters

class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        char_count = {}

        for ch in chars:
            char_count[ch] = char_count.get(ch, 0) + 1

        total = 0

        for word in words:
            word_count = {}

            for ch in word:
                word_count[ch] = word_count.get(ch, 0) +1

            can_form = True

            for ch in word_count:
                if word_count[ch] > char_count.get(ch, 0):
                    can_form =False
                    break

            if can_form:
                total += len(word)

        return total


# Example usage
if __name__ == "__main__":
    solution = Solution()
    words = ["cat", "bt", "hat", "tree"]
    chars = "atach"
    print(solution.countCharacters(words, chars))
