class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        

        start = 0
        tank = 0
        total = 0


        for i in range(len(gas)):

            gain = gas[i] - cost[i]

            tank += gain
            total += gain

            if tank < 0:
                start = i + 1
                tank = 0


        return start if total >= 0 and start < len(gas) else -1