class Solution:
    def isPalindrome(self, x: int) -> bool:
        

        if x < 0:
            return False

        x_string = str(x)

        for i in range(len(x_string) // 2):
            left, right = i, len(x_string) - i - 1

            if x_string[left] != x_string[right]:
                return False

        return True