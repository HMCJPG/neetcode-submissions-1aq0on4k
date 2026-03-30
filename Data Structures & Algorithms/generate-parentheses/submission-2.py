class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

        res = []

        def permute(current: str, open_count: int, close_count: int):
            if len(current) == 2*n:
                if open_count == close_count:
                    res.append(current)
                    return

            if open_count < n:
                permute(current + '(', open_count + 1, close_count)

            if close_count < open_count:
                permute(current + ')', open_count, close_count + 1)

        permute("", 0,0)

        return res