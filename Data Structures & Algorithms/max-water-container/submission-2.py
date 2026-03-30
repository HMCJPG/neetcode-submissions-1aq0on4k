class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        lp, rp = 0, len(heights) - 1

        max_amount = 0

        while lp <= rp:

            local_max = (rp - lp) * min(heights[lp], heights[rp])

            max_amount = max(local_max, max_amount)

            if heights[lp] < heights[rp]:
                lp += 1
            else:
                rp -= 1

        return max_amount