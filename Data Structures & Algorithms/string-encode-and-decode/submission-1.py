class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += word
            encoded += '~'
        return encoded
    def decode(self, s: str) -> List[str]:
        
        word = ""
        wordList = []

        for ch in s:
            if ch == '~':
                wordList.append(word)
                word = ""
            else:
                word += ch
        return wordList
