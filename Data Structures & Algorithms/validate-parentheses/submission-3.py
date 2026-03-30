class Solution:
    def isValid(self, s: str) -> bool:
        
        bMap = {"(":")", "{":"}", "[":"]"}
        stack = []


        for c in s:
            if c in bMap:
                stack.append(c)
            else:
                if not stack:
                    return False
                elif bMap[stack[-1]] == c:
                    stack.pop()
                else:
                    return False

        return not stack