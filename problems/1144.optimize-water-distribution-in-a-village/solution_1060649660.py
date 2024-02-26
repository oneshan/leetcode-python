# 1144 - Optimize Water Distribution in a Village
# Date: 2023-09-28
# Runtime: 419 ms, Memory: 23.1 MB
# Submission Id: 1060649660


from collections import defaultdict
import heapq

class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        graph = defaultdict(list)
        for idx, weight in enumerate(wells, 1):
            graph[0].append((weight, idx))
        
        for p, q, weight in pipes:
            graph[p].append((weight, q))
            graph[q].append((weight, p))
            
        mst_set = set()
        heapq.heapify(graph[0])
        edge_heap = graph[0]
        
        total_cost = 0
        while len(mst_set) < n:
            weight, node = heapq.heappop(edge_heap)
            if node not in mst_set:
                total_cost += weight
                mst_set.add(node)
                for new_weight, neighbor in graph[node]:
                    if neighbor not in mst_set:
                        heapq.heappush(edge_heap, (new_weight, neighbor))
        return total_cost