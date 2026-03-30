class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        n = len(nums)

        min_prod = nums[0]
        max_prod = nums[0]
        ans = nums[0]

        for i in range(1, n):

            choices = (nums[i], min_prod * nums[i], max_prod * nums[i])

            min_prod = min(choices)
            max_prod = max(choices)

            ans = max(max_prod, ans)

        return ans