class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        aggregate = []

        for row in matrix:
            for num in row:
                aggregate.append(num)

        left, right = 0, len(aggregate) - 1

        while left <= right:

            mid = (left + right) // 2

            if aggregate[mid] == target:
                return True

            elif aggregate[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return False

