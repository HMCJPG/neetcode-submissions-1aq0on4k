class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        carCount = len(position)
        ttd = [0]*carCount

        cars = [(p, (target - p) / s) for p, s in zip(position, speed)]


        cars.sort(reverse = True)

        fleets = 0
        prev_time = 0

        for _, time in cars:
            if time > prev_time:
                fleets += 1
                prev_time = time
        
        return fleets

        