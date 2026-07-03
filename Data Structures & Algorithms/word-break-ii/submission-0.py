from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        wordSet = set(wordDict)
        memo = {}

        def dfs(start:int) -> List[str]:
            if start in memo:
                return memo[start]
            if start == len(s):
                return [""]

            sentences = []

            for word in wordDict:
                if s.startswith(word, start):
                    remaining = dfs(start + len(word))

                    for sub in remaining:
                        sentence = word + (" " + sub if sub else "")
                        sentences.append(sentence)

            memo[start] = sentences
            return sentences

        return dfs(0)