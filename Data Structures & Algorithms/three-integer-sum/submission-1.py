from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        if len(nums) < 3:
            return []


        seen = set()

        nums.sort()

        for i in range(0, len(nums) - 2):
            

            lp = i + 1
            rp = len(nums) - 1

            while lp < rp:

                currentVal = nums[i] + nums[lp] + nums[rp]
                if currentVal == 0:
                    candidate = tuple(sorted((nums[i], nums[lp], nums[rp])))
                    if candidate not in seen:
                        seen.add(candidate)
                    lp += 1
                    rp -= 1

                        

                elif currentVal < 0:
                    lp += 1
                else:
                    rp -= 1


        
        return [list(t) for t in seen]
            

