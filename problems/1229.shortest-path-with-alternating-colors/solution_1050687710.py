# 1229 - Shortest Path with Alternating Colors
# Date: 2023-09-16
# Runtime: 79 ms, Memory: 16.6 MB
# Submission Id: 1050687710


from collections import defaultdict, deque

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        ans = [-1] * n
        RED, BLUE = 0, 1
        
        graph = defaultdict(list)
        for a, b in redEdges:
            graph[(a, RED)].append(b)
        for a, b in blueEdges:
            graph[(a, BLUE)].append(b)
            
        queue = deque([(0, RED), (0, BLUE)])
        seen = {(0, RED), (0, BLUE)}
        step = 0
        while queue:
            for _ in range(len(queue)):
                node, color = queue.popleft()
                if ans[node] == -1:
                    ans[node] = step
                next_color = 1 - color
                for neighbor in graph[(node, color)]:
                    if (neighbor, next_color) not in seen:
                        seen.add((neighbor, next_color))
                        queue.append((neighbor, next_color))
            step += 1
        return ans