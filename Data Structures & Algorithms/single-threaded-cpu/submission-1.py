class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        for i,task in enumerate(tasks):
            task.append(i)

        tasks.sort(key = lambda task: task[0])

        result = []
        min_heap = []

        current_time = tasks[0][0]
        task_idx = 0

        while min_heap or task_idx < len(tasks):

            while task_idx < len(tasks) and current_time >= tasks[task_idx][0]:
                enqueue_time , processing_time, original_idx = tasks[task_idx]
                heapq.heappush(min_heap, (processing_time, original_idx))
                task_idx += 1

            if not min_heap:
                current_time = tasks[task_idx][0]

            else:
                processing_time, original_idx = heapq.heappop(min_heap)
                current_time += processing_time
                result.append(original_idx)

        return result
