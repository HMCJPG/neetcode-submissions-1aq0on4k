import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        g = math.gcd(len(str1), len(str2))

        candidate = str1[:g]

        if str1 == candidate * (len(str1) // g) and \
            str2 == candidate * (len(str2) // g):
            return candidate
        return ""