class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        total = sum(stones)
        target = total // 2

        possible = {0}

        for stone in stones:
            next_possible = set(possible)

            for val in possible:
                next_possible.add(val + stone)
            possible = next_possible


        best = max(p for p in possible if p <= target)


        return total - 2 * best