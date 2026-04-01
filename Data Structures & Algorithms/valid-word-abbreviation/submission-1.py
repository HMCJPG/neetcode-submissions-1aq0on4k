class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        

        wordPointer = 0
        abbrPointer = 0

        while wordPointer < len(word) and abbrPointer < len(abbr):
            c = abbr[abbrPointer]

            if c.isalpha():
                if word[wordPointer] != c:
                    return False

                wordPointer += 1
                abbrPointer += 1

            else:
                if c == '0':
                    return False

                num = 0
                while abbrPointer < len(abbr) and abbr[abbrPointer].isdigit():
                    num = num * 10 + int(abbr[abbrPointer])
                    abbrPointer += 1

                wordPointer += num

        return wordPointer == len(word) and abbrPointer == len(abbr)






            