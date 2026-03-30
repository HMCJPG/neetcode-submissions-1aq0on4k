from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        taken = 0

        unlocks = defaultdict(list)
        degree = [0] * numCourses

        for a,b in prerequisites:
            unlocks[b].append(a)
            degree[a] += 1

        queue = deque()

        for i in range(numCourses):
            if degree[i] == 0:
                queue.append(i)

        while queue:
            taken += 1
            course = queue.popleft()
            for neighbor in unlocks[course]:
                degree[neighbor] -= 1

                if degree[neighbor] == 0:
                    queue.append(neighbor)

        return numCourses == taken







