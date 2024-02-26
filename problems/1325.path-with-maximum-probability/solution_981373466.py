# 1325 - Path with Maximum Probability
# Date: 2023-06-28
# Runtime: 649 ms, Memory: 29.3 MB
# Submission Id: 981373466


from collections import defaultdict
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for prob, (p, q) in zip(succProb, edges):
            graph[p].append((q, prob))
            graph[q].append((p, prob))
            
        max_prob = [0] * n
        max_prob[start] = 1.0
        
        pq = [(-1.0, start)]
        while pq:
            prob, node = heapq.heappop(pq)
            if node == end:
                return -prob
            
            for neighbor, next_prob in graph[node]:
                if -prob * next_prob > max_prob[neighbor]:
                    max_prob[neighbor] = -prob * next_prob
                    heapq.heappush(pq, (-max_prob[neighbor], neighbor))
        return 0.0