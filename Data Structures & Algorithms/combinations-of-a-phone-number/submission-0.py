class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []

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

        res = []

        def backtrack(index, path):
            if index == len(digits):
                res.append(path)
                return




            current_digit = digits[index]
            for letter in lets[current_digit]:
                backtrack(index + 1, path + letter)


        backtrack(0, "")
        return res