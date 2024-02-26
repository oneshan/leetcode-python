# 1962 - Single-Threaded CPU
# Date: 2022-11-19
# Runtime: 5490 ms, Memory: 63.9 MB
# Submission Id: 846388720


import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        enqueue = []  # min heap of (enqueue_time, task_id)
        available = []  # min heap of (process_time, task_id)
        task_time = {}  # {task_id: process_time}
        
        for idx, (enqueue_time, process_time) in enumerate(tasks):
            task_time[idx] = process_time
            heapq.heappush(enqueue, (enqueue_time, idx))
        
        ans = [0] * len(tasks)
        ans_idx = curr_time = 0
        while ans_idx < len(tasks):
            if not available and curr_time < enqueue[0][0]:
                curr_time = enqueue[0][0]
            while enqueue and curr_time >= enqueue[0][0]:
                _, idx = heapq.heappop(enqueue)
                heapq.heappush(available, (task_time[idx], idx))
                
            process_time, idx = heapq.heappop(available)
            curr_time += process_time
            ans[ans_idx] = idx
            ans_idx += 1

        return ans