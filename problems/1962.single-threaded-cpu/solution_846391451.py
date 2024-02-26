# 1962 - Single-Threaded CPU
# Date: 2022-11-19
# Runtime: 2228 ms, Memory: 63.4 MB
# Submission Id: 846391451


import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        available = []  # min heap of (process_time, task_id)
        sorted_task = sorted((enqueue_time, process_time, task_id)
                             for task_id, (enqueue_time, process_time) in enumerate(tasks))
        n = len(tasks)
        
        ans = [0] * n
        used_idx = curr_time = 0
        for idx in range(n):
            if not available and curr_time < sorted_task[used_idx][0]:
                curr_time = sorted_task[used_idx][0]
            while used_idx < n and curr_time >= sorted_task[used_idx][0]:
                heapq.heappush(available, (sorted_task[used_idx][1], sorted_task[used_idx][2]))
                used_idx += 1
                
            process_time, task_id = heapq.heappop(available)
            curr_time += process_time
            ans[idx] = task_id

        return ans