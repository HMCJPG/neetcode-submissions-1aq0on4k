from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        

        unlocks = defaultdict(list)
        degree = [0] * numCourses
        res = []
        taken = 0


        for a,b in prerequisites:

            unlocks[b].append(a)
            degree[a] += 1

        queue = deque()

        for i in range(len(degree)):
            if degree[i] == 0:
                queue.append(i)


        while queue:
            course = queue.popleft()
            res.append(course)
            taken += 1

            for neighbor in unlocks[course]:
                degree[neighbor] -= 1

                if degree[neighbor] == 0:
                    queue.append(neighbor)

        return res if len(res) == numCourses else []





