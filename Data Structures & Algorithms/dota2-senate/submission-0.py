from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        radiant_queue = deque()
        dire_queue = deque()

        # Store indices for each party's senators:

        for i, senator in enumerate(senate):
            if senator == 'R':
                radiant_queue.append(i)
            else:
                dire_queue.append(i)

        
        # Simumate the voting process

        while radiant_queue and dire_queue:
            r_index = radiant_queue.popleft()
            d_index = dire_queue.popleft()

            if r_index < d_index:
                radiant_queue.append(r_index + len(senate))
            else:
                dire_queue.append(d_index + len(senate))

        return "Radiant" if radiant_queue else "Dire"