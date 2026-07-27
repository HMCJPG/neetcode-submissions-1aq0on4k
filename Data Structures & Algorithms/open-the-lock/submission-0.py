class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        start = "0000"
        dead = set(deadends)

        if start in dead:
            return -1

        if start == target:
            return 0


        queue = deque([start])
        seen = set([start])
        steps = 0

        while queue:
            
            steps += 1

            for _ in range(len(queue)):
                current = queue.popleft()

                for i in range(4):

                    digit = int(current[i])
                    for move in (-1, 1):
                        new_digit = (digit + move) % 10

                        next_state = current[:i] + str(new_digit) + current[i + 1:]

                        if next_state in dead or next_state in seen:
                            continue

                        if next_state == target:
                            return steps

                        seen.add(next_state)
                        queue.append(next_state)


        return -1









