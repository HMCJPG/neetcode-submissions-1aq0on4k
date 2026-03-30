class Solution:
    def trap(self, height: List[int]) -> int:
        if not isinstance(height, list) or len(height) < 3:
            return 0
        
        lp = 0
        stored_water = 0
        n = len(height)

        while lp < n - 1:
            rp = lp + 1

            # First try to find a wall >= left wall
            found = False
            for i in range(lp + 1, n):
                if height[i] >= height[lp]:
                    rp = i
                    found = True
                    break
            
            # If no wall >= left wall, use tallest wall to the right
            if not found:
                rp = lp + 1
                for i in range(lp + 1, n):
                    if height[i] > height[rp]:
                        rp = i

            # Now, compute trapped water between lp and rp
            bounded_height = min(height[lp], height[rp])
            for i in range(lp + 1, rp):
                stored_water += max(0, bounded_height - height[i])
            
            # Move lp forward
            lp = rp

        return stored_water
