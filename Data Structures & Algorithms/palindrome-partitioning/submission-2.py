class Solution:
    def partition(self, s: str) -> List[List[str]]:
        

        path = []
        res = []

        def palindromic(s):
            return s == s[::-1]

        def backtrack(start):

            if start == len(s):
                res.append(path[:])

            for end in range(start + 1, len(s) + 1):

                sub = s[start:end]
                if palindromic(sub):
                    path.append(sub)
                    backtrack(end)
                    path.pop()

        backtrack(0)

        return res
            