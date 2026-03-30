class Solution:
    def validPalindrome(self, s: str) -> bool:
        

        case1 = True
        case2 = True
        case3 = True
        left, right = 0, len(s) - 1

        while left <= right:

            if s[left] != s[right]:
                case1 = False
                break
            left += 1
            right -= 1
        



        misses = 1

        while left <= right:
            if s[left] != s[right] and misses > 0:
                misses -= 1
                left += 1

            elif s[left] != s[right] and misses == 0:
                case2 = False
                break

            else:
                left += 1
                right -= 1

        left, right = 0, len(s) - 1
        misses = 1

        while left <= right:
            if s[left] != s[right] and misses > 0:
                misses -= 1
                right -= 1

            elif s[left] != s[right] and misses == 0:
                case3 = False
                break

            else:
                left += 1
                right -= 1

        if case1 or case2 or case3:
            return True
        return False



