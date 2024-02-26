# 1710 - Find Servers That Handled Most Number of Requests
# Date: 2023-11-01
# Runtime: 2671 ms, Memory: 37.8 MB
# Submission Id: 1089102260


from sortedcontainers import SortedList
import heapq

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        record = [0] * k
        used_s = []
        free_s = SortedList(range(k))
        
        for idx, start in enumerate(arrival):
            end = start + load[idx]
            while used_s and used_s[0][0] <= start:
                _, server = heapq.heappop(used_s)
                free_s.add(server)
            
            if free_s:
                left, right = 0, len(free_s)
                while left < right:
                    mid = (left + right) // 2
                    if free_s[mid] >= (idx % k):
                        right = mid
                    else:
                        left = mid + 1
    
                server = free_s[left] if left < len(free_s) else free_s[0]
                free_s.remove(server)
                heapq.heappush(used_s, [end, server])
                record[server] += 1
            
        max_record = max(record)
        return [i for i in range(k) if record[i] == max_record]