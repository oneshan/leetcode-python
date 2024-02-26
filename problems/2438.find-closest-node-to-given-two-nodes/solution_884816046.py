# 2438 - Find Closest Node to Given Two Nodes
# Date: 2023-01-25
# Runtime: 1724 ms, Memory: 32.5 MB
# Submission Id: 884816046


from collections import deque

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        
        def bfs(start):
            queue = deque([start])
            seen = {start, -1}
            distance = [float('inf')] * n
            step = 0
            while queue:
                node = queue.popleft()
                distance[node] = step
                if edges[node] not in seen:
                    queue.append(edges[node])
                    seen.add(edges[node])
                step += 1
            return distance
        
        d1 = bfs(node1)
        d2 = bfs(node2)
        ans, min_dist = -1, float('inf')
        for i in range(n):
            curr_max = max(d1[i], d2[i])
            if min_dist > curr_max:
                ans, min_dist = i, curr_max
        return ans