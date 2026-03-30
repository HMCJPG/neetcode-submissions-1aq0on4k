from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        most_expensive = max(task_counts.values())
        n_max = sum(1 for v in task_counts.values() if v == most_expensive)

        # The minimum cycles needed (may be less if all slots are filled)
        min_cycles = (most_expensive - 1) * (n + 1) + n_max

        # The answer is the larger of total task count and calculated minimum
        return max(min_cycles, len(tasks))
