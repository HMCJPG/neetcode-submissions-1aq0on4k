class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        

        trips.sort(key = lambda t: t[1])

        dropoff_heap = []
        current_passengers = 0

        for num_passengers, pickup_loc, dropoff_loc in trips:

            while dropoff_heap and dropoff_heap[0][0] <= pickup_loc:
                current_passengers -= heapq.heappop(dropoff_heap)[1]


            current_passengers += num_passengers

            if current_passengers > capacity:
                return False

            heapq.heappush(dropoff_heap, (dropoff_loc, num_passengers))


        return True