# 1710 - Find Servers That Handled Most Number of Requests
# Date: 2023-11-01
# Runtime: 1024 ms, Memory: 37.2 MB
# Submission Id: 1089160912


import heapq

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        record = [0] * k
        used_s = []
        free_s = list(range(k))
        heapq.heapify(free_s)
        
        for idx, start in enumerate(arrival):
            end = start + load[idx]
            while used_s and used_s[0][0] <= start:
                _, server = heapq.heappop(used_s)
                heapq.heappush(free_s, idx + (server-idx) % k)
                
            if free_s:
                server = heapq.heappop(free_s) % k
                heapq.heappush(used_s, [end, server])
                record[server] += 1
            
        max_record = max(record)
        return [i for i in range(k) if record[i] == max_record]