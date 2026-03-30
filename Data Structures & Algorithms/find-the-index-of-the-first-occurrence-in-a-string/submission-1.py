from collections import defaultdict


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:


        firstLet = needle[0]
        size = len(needle)

        for i in range(len(haystack)):
            if haystack[i] == firstLet:
                if i + size <= len(haystack):
                    if haystack[i:i + size] == needle:
                        return i

        return -1



        