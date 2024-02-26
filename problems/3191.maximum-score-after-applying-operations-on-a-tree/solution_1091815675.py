# 3191 - Maximum Score After Applying Operations on a Tree
# Date: 2023-11-05
# Runtime: 1107 ms, Memory: 48.4 MB
# Submission Id: 1091815675


class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        n = len(values)
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def recur(node, prev):
            if node and len(graph[node]) == 1:
                return values[node]
            
            total_delete = 0
            for child in graph[node]:
                if child == prev:
                    continue
                _delete = recur(child, node)
                total_delete += _delete
            return min(total_delete, values[node])

        total_delete = recur(0, -1)
        return sum(values) - total_delete