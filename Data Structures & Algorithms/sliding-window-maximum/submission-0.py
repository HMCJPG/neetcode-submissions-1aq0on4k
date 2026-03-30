from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        

        res = []
        q = deque()


        for i, num in enumerate(nums):

            while q and nums[i] >= nums[q[-1]]:
                q.pop()

            q.append(i)

            if q[0] <= i - k:
                q.popleft()

            if i >= k - 1:
                res.append(nums[q[0]])

        return res

            













