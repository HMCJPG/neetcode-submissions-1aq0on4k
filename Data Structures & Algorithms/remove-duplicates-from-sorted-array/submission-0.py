class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        seen = set()
        marked = []

        for i, num in enumerate(nums):
            if num in seen:
                marked.append(i)
            else:
                seen.add(num)

        for i in range(len(marked) - 1, -1, -1):
            del nums[marked[i]]

        return len(nums)