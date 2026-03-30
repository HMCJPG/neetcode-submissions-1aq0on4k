class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {} #initialize our hashmap, to hold our values and locations
        # good for indices

        for i in range(len(nums)): # iterate 
            cmt = target - nums[i] # store a complement value, basically we want to see if we ever have
            # a pairing's other complement

            if cmt in seen: #if we've seen tjis garbage before
                return [seen[target - nums[i]], i] #send back the location of the complemnt and i.
                #necessarily we'll have seen teh complemetn first

            seen[nums[i]] = i #add in the value into see, and say we say it at i's location

