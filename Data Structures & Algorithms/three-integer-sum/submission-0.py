class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        seen = set()
        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            lp = i + 1
            rp = len(nums) - 1

            while lp < rp:
                sum = nums[i] + nums[lp] + nums[rp]

                if sum == 0:
                    triple = (nums[i], nums[lp], nums[rp])
                    if triple not in seen:
                        res.append([nums[i], nums[lp], nums[rp]])
                        seen.add(triple)
                    lp += 1
                    rp -= 1

                    # subtree logic one: check if we alr have seen this
                elif sum < 0:
                    lp += 1
                else:
                    rp -= 1
        return res