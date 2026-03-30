class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
  #      if heights not List:
#            return 0

        lp = 0
        rp = len(heights) - 1
        globalMax = (rp - lp) * min(heights[lp], heights[rp])

        while lp < rp:
            if heights[lp] < heights[rp]:
                lp += 1
            else:
                rp -= 1
            currentMax = (rp - lp) * min(heights[lp], heights[rp])

            globalMax = max(currentMax, globalMax)

        return globalMax
                
            


