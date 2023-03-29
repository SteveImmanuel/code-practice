class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_dict = Counter(tasks)
        task_heap = [[-value, key, None] for key, value in task_dict.items()]
        heapq.heapify(task_heap)
        
        current_time = 1
        while len(task_heap) > 0:
            task = heapq.heappop(task_heap)
            task_buffer = []
            if not (task[2] is None or task[2] <= current_time):
                heapq.heappush(task_buffer, task)
                while len(task_heap) > 0:
                    task = heapq.heappop(task_heap)
                    if task[2] is None or task[2] <= current_time:
                        break
                    else:
                        heapq.heappush(task_buffer, task)
                if len(task_heap) == 0 and not (task[2] is None or task[2] <= current_time):
                    task_heap = task_buffer
                    task_buffer = []
                    task = heapq.heappop(task_heap)
                    current_time = task[2]

            task[0] += 1
            task[2] = current_time + n + 1
            current_time += 1
            if task[0] != 0:
                heapq.heappush(task_heap, task)
            while len(task_buffer) > 0:
                heapq.heappush(task_heap, heapq.heappop(task_buffer))

        return current_time - 1