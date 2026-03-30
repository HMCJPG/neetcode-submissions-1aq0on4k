class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        
        lets = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"

        }

        if not digits:
            return []


        n = len(digits)

        res = []
        path = []
        def backtrack(index, path):

            if index == n:
                res.append(path)

                return

            digit = digits[index]
            for c in lets[digit]:
                backtrack(index + 1, path + c)


        backtrack(0,"")

        return res











