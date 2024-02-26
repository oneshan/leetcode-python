# 2353 - Maximum Score of a Node Sequence
# Date: 2023-09-02
# Runtime: 1975 ms, Memory: 45.1 MB
# Submission Id: 1038359246


from collections import defaultdict
import heapq

class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        for a, b in edges:            
            heapq.heappush(graph[a], (scores[b], b))
            heapq.heappush(graph[b], (scores[a], a))
            if len(graph[a]) == 4:
                heapq.heappop(graph[a])
            if len(graph[b]) == 4:
                heapq.heappop(graph[b])
        
        ans = -1
        for a, b in edges:
            for score_c, c in graph[a]:
                for score_d, d in graph[b]:
                    if len(set([a, b, c, d])) == 4:
                        ans = max(ans, scores[a] + scores[b] + score_c + score_d)
        return ans