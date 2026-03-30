class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        

        finalIndexes = {c:i for i,c in enumerate(s)}

        start = end = 0

        res = []

        for i, c in enumerate(s):

            end = max(end, finalIndexes[c])

            if i == end:
                res.append(end - start + 1)
                start = i + 1

        return res