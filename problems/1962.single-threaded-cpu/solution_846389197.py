# 1962 - Single-Threaded CPU
# Date: 2022-11-19
# Runtime: 5914 ms, Memory: 63 MB
# Submission Id: 846389197


import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        enqueue = []  # min heap of (enqueue_time, task_id)
        available = []  # min heap of (process_time, task_id)
        task_time = {}  # {task_id: process_time}
        
        for task_id, (enqueue_time, process_time) in enumerate(tasks):
            task_time[task_id] = process_time
            heapq.heappush(enqueue, (enqueue_time, task_id))
        
        ans = [0] * len(tasks)
        curr_time = 0
        for idx in range(len(tasks)):
            if not available and curr_time < enqueue[0][0]:
                curr_time = enqueue[0][0]
            while enqueue and curr_time >= enqueue[0][0]:
                _, task_id = heapq.heappop(enqueue)
                heapq.heappush(available, (task_time[task_id], task_id))
                
            process_time, task_id = heapq.heappop(available)
            curr_time += process_time
            ans[idx] = task_id

        return ans