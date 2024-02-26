# 0744 - Network Delay Time
# Date: 2023-09-24
# Runtime: 396 ms, Memory: 18.6 MB
# Submission Id: 1057879291


from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u-1].append((v-1, w))
        
        heap = [(k-1, 0)]
        distances = [float('inf')] * n
        distances[k-1] = 0
        
        while heap:
            node, curr_dist = heapq.heappop(heap)
            if curr_dist > distances[node]:
                continue
            for neighbor, weight in graph[node]:
                dist = curr_dist + weight
                if dist < distances[neighbor]:
                    distances[neighbor] = dist
                    heapq.heappush(heap, (neighbor, dist))
        
        ans = max(distances)
        return ans if ans < float('inf') else -1