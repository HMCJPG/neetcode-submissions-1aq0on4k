class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        n = len(s)
        if n % 2 == 0:
            midIndex = int(n / 2)
        else:
            midIndex = int(n // 2)

        for i in range(midIndex):
            s[i],s[n - i - 1] = s[n - i - 1], s[i]
        