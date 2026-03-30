from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        tracked = defaultdict(int)
        left_index = 0
        right_index = 0
        max_window = 0

        for i in range(len(s)):

            tracked[s[right_index]] += 1
            right_index += 1

            window_size = right_index - left_index
            biggest = max(tracked.values())
            replacements = window_size - biggest

            while replacements > k:
                tracked[s[left_index]] -= 1
                left_index += 1
                window_size = right_index - left_index
                biggest = max(tracked.values())
                replacements = window_size - biggest

            max_window = max(max_window, window_size)
            

                
        return max_window
