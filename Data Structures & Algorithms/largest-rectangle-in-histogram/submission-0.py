class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        max_area = 0
        stack = []

        heights. append(0)

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]

                if not stack:
                    width = i

                else:
                    width = i - stack[-1] - 1
                
                area = height * width
                max_area = max(max_area, area)

            stack.append(i)

        return max_area