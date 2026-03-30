class Solution:
    def isValid(self, s: str) -> bool:
        
        if not isinstance(s, str) or len(s)%2 != 0 or s == "":
            return False

        stack = []
        bMap = {'(':')', '{':'}', '[':']' }

        for c in s:
            if c in bMap:
                stack.append(c)
            elif c in bMap.values():
                if not stack:
                    return False

                topOfStack = stack.pop()
                if not c == bMap[topOfStack]: #Im trying ti match the value back to the key
                    return False


        return len(stack)==0