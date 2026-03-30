class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        
        m, n = len(nums1), len(nums2)


        left, right = 0, m

        while left <= right:

            i = (left + right) // 2
            j = (m + n + 1) // 2 - i

            nums1left = float('-inf') if i == 0 else nums1[i - 1]
            nums1right = float('inf') if i == m else nums1[i]
            nums2left = float('-inf') if j == 0 else nums2[j - 1]
            nums2right = float('inf') if j == n else nums2[j]


            if nums1left <= nums2right and nums2left <= nums1right:

                if (m + n) % 2 == 0:
                    return ((max(nums1left, nums2left) + min(nums1right, nums2right)) / 2.0)

                else:
                    return max(nums1left, nums2left)

                
            elif nums1left > nums2right:
                right = i - 1
            
            else:
                left = i + 1








