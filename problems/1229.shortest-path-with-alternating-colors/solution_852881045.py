# 1229 - Shortest Path with Alternating Colors
# Date: 2022-12-01
# Runtime: 212 ms, Memory: 14.2 MB
# Submission Id: 852881045


from collections import defaultdict

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        ans = [-1] * n
        
        rgraph = defaultdict(list)
        for a, b in redEdges:
            rgraph[a].append(b)
        bgraph = defaultdict(list)
        for a, b in blueEdges:
            bgraph[a].append(b)

        graph = [rgraph, bgraph]
        
        queue = deque([(0, 0), (0, 1)])
        seen = {(0, 0), (0, 1)}
        step = 0
        while queue:
            for _ in range(len(queue)):
                node, color = queue.popleft()
                ans[node] = min(ans[node], step) if ans[node] != -1 else step
                color ^= 1
                for neighbor in graph[color][node]:
                    if (neighbor, color) not in seen:
                        seen.add((neighbor, color))
                        queue.append((neighbor, color))
            step += 1
        
        return ans