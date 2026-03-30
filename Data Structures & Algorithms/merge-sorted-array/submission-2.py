import heapq

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        heap = []
        zeroCounter = 0
        invalid = len(nums1) - m


        for num in nums1:
            if num == 0 and zeroCounter < invalid:
                zeroCounter += 1
            elif num == 0 and zeroCounter >= invalid:
                heapq.heappush(heap, num)   
            elif num != 0:
                heapq.heappush(heap, num)

        for num in nums2:
            heapq.heappush(heap, num)

        for i in range(len(nums1)):
            if heap:
                nums1[i] = heapq.heappop(heap)


