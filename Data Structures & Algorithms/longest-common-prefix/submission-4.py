class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        prefix = ""

        word = strs[0]

        for i in range(len(word)):
            char = word[i]
            for string in strs:
                if i >= len(string) or string[i] != char:
                    return prefix
            prefix += char
        return prefix