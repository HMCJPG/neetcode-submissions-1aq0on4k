from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        tracked = defaultdict(int)
        max_size = 0
        left_index = 0
        right_index = 0

        for i in range(len(s)):

            char = s[i]
            tracked[char] += 1
            right_index += 1

            while tracked[char] > 1:
                tracked[s[left_index]] -= 1
                left_index += 1

            size = right_index - left_index
            max_size = max(size, max_size)

        return max_size
                

