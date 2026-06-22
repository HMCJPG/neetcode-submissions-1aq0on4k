class Solution:
    def reorganizeString(self, s: str) -> str:
        
        n = len(s)
        counts = {}

        for char in s:
            counts[char] = counts.get(char, 0) + 1

        sorted_chars = sorted(counts.keys(), key = lambda x: -counts[x])

        if counts[sorted_chars[0]] > (n + 1) // 2:
            return ""


        res = [None] * n
        index = 0

        for char in sorted_chars:
            for _ in range(counts[char]):

                if index >= n:
                    index = 1
                res[index] = char
                index += 2

        return "".join(res)

        