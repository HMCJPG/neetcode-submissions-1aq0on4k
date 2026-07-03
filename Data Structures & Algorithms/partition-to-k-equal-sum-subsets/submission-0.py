class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        total = sum(nums)

        if total % k != 0:
            return False


        target = total // k
        nums.sort(reverse = True)
        used = [False] * len(nums)

        def backtrack(start, cur_sum, subsets_formed):
            if subsets_formed == k:
                return True
            
            if cur_sum == target:
                return backtrack(0,0, subsets_formed + 1)

            for i in range(start, len(nums)):
                if not used[i] and cur_sum + nums[i] <= target:
                    used[i] = True
                    if backtrack(i + 1, cur_sum + nums[i], subsets_formed):
                        return True
                    used[i] = False

                    if cur_sum == 0:
                        break

            return False


        return backtrack(0,0,0)









