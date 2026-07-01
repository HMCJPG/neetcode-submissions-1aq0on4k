class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        

        res = []
        def backtrack(index, current_combo):

            if len(current_combo) == k:
                res.append(current_combo.copy())
                return

            

            for next_num in range(index + 1, n + 1):

                current_combo.append(next_num)
                backtrack(next_num, current_combo)
                current_combo.pop()

        backtrack(0, [])
        return res
