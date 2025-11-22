# Leetcode no.127 - Word Ladder

from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        queue = deque()
        queue.append((beginWord, 1))  # (current_word, current_length)
        
        while queue:
            current_word, current_length = queue.popleft()
            if current_word == endWord:
                return current_length
            for i in range(len(current_word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    if ch == current_word[i]:
                        continue
                    new_word = current_word[:i] + ch + current_word[i+1:]
                    if new_word in word_set:
                        queue.append((new_word, current_length + 1))
                        word_set.remove(new_word)  # Avoid revisiting
        return 0

# Example usage:
if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    solution = Solution()
    result = solution.ladderLength(beginWord, endWord, wordList)
    print(result)  # Output: 5 (hit -> hot -> dot -> dog -> cog)