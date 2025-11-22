# Leetcode no.126 - Word Ladder II

from collections import deque
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        word_set = set(wordList)
        if endWord not in word_set:
            return []
        result = []
        queue = deque()
        queue.append([beginWord]) 
        
        while queue:
            level_size = len(queue)
            choosen_words = set()
            for _ in range(level_size):
                sequence = queue.popleft()
                last_word = sequence[-1]
                if last_word == endWord:
                    result.append(sequence)
                for i in range(len(last_word)):
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        if ch == last_word[i]:
                            continue
                        new_word = last_word[:i] + ch + last_word[i+1:]
                        if new_word in word_set:
                            new_sequence = sequence + [new_word]
                            queue.append(new_sequence)
                            choosen_words.add(new_word)
                
            for word in choosen_words:
                word_set.remove(word)
        return result

# Example usage:
if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    solution = Solution()
    result = solution.findLadders(beginWord, endWord, wordList)
    for seq in result:
        print(seq)  # Output: All shortest transformation sequences from "hit" to "cog"