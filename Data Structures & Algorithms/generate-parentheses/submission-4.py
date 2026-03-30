class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

        res = []

        def backtrack(curr, open_left, open_right):

            if open_left == 0 and open_right == 0:
                res.append(curr)
                return

            if open_left > 0:
                backtrack(curr + "(", open_left - 1, open_right)

            if open_right > open_left:
                backtrack(curr + ")", open_left, open_right - 1)

        backtrack("", n, n)

        return res