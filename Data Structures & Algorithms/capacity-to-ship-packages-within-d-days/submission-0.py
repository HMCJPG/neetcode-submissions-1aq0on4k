class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        

        def jobPossible(capacity: int) -> bool:
            days_used = 1
            current_load = 0
    
            for weight in weights:
            # If a single package is heavier than the total capacity, it's impossible
                if weight > capacity:
                    return False
                
                if current_load + weight <= capacity:
                # Add to the current day's truck
                    current_load += weight
                else:
                # Start a new day
                    days_used += 1
                    current_load = weight
            
            return days_used <= days

        left, right = max(weights), sum(weights)

        while left <= right:
            middle = int((left + right) // 2)

            if jobPossible(middle):
                right = middle - 1
            else:
                left = middle + 1

        return left











