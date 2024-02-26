# 1229 - Shortest Path with Alternating Colors
# Date: 2023-02-11
# Runtime: 75 ms, Memory: 14.2 MB
# Submission Id: 895739271


from collections import defaultdict

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
                ans[node] = step if ans[node] == -1 else min(ans[node], step)
                nxt_color = BLUE if color == RED else RED
                for neighbor in graph[(node, nxt_color)]:
                    if (neighbor, nxt_color) not in seen:
                        seen.add((neighbor, nxt_color))
                        queue.append((neighbor, nxt_color))
            step += 1
        return ans