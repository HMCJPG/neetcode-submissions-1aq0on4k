class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        n = len(ratings)
        total_candies = n

        i = 0

        while i < n:
            if i + 1 < n and ratings[i] == ratings[i + 1]:
                i += 1
                continue

            increase_length = self._process_increase(ratings, i)
            total_candies += self._sum_increase(increase_length)
            i += increase_length

            decrease_length = self._process_decrease(ratings, i)
            total_candies += self._sum_decrease(decrease_length)

            overlap = min(increase_length, decrease_length)
            total_candies -= overlap

            i += decrease_length

            if increase_length == 0 and decrease_length == 0:
                i += 1

        return total_candies

    def _process_increase(self, ratings: List[int], start: int) -> int:
        count = 0
        i = start

        while i + 1 < len(ratings) and ratings[i + 1] > ratings[i]:
            count += 1
            i += 1
        return count

    def _process_decrease(self, ratings: List[int], start: int) -> int:
        count = 0
        i = start

        while i + 1 < len(ratings) and ratings[i + 1] < ratings[i]:
            count += 1
            i += 1
        return count

    def _sum_increase(self, length: int) -> int:
        return length * (length + 1) // 2

    def _sum_decrease(self, length: int) -> int:
        return length * (length + 1) // 2
       

