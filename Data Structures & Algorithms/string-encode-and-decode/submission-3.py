class Solution:

    def encode(self, strs: List[str]) -> str:

        master = ""

        for string in strs:
            master += string
            master += "~"
        return master

    def decode(self, s: str) -> List[str]:

        strs = []
        current = ""
        for char in s:
            if char == "~":
                strs.append(current)
                current = ""
            else:
                current += char

        return strs
