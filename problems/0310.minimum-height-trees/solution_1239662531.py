# 0310 - Minimum Height Trees
# Date: 2024-04-23
# Runtime: 411 ms, Memory: 29.9 MB
# Submission Id: 1239662531


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return list(range(n))

        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        leaves = [a for a in graph if len(graph[a]) == 1]
        queue = deque(leaves)
        seen = set(leaves)
        while queue and n > 2:
            for _ in range(len(queue)):
                node = queue.popleft()
                n -= 1
                for neighbor in graph[node]:
                    graph[neighbor].discard(node)
                    if len(graph[neighbor]) == 1:
                        queue.append(neighbor)
        return queue