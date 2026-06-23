class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        counts = {'a': a, 'b': b, 'c': c}
        result = []

        def next_char(last, prev_count):
            best_char = None
            best_count = 0

            for ch in ('a','b','c'):
                if counts[ch] == 0:
                    continue

                if ch == last and prev_count == 2:
                    continue

                if counts[ch] > best_count:
                    best_count = counts[ch]
                    best_char = ch

            return best_char

        last_char = None
        repeat_count = 0

        while True:
            ch = next_char(last_char, repeat_count)
            if not ch:
                break

            result.append(ch)
            counts[ch] -= 1

            if ch == last_char:
                repeat_count += 1
            else:
                last_char = ch
                repeat_count = 1

        return ''.join(result)

