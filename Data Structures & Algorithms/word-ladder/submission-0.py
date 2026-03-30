from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0



        queue = deque([(beginWord, 1)])

        while queue:
            word, steps = queue.popleft()

            if word == endWord:
                return steps

            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c != word[i]:
                        next_word = word[:i] + c + word[i + 1:]
                        if next_word in wordSet:
                            queue.append((next_word, steps + 1))
                            wordSet.remove(next_word)


        return 0









            