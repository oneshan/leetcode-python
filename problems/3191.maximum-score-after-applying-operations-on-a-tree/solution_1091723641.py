# 3191 - Maximum Score After Applying Operations on a Tree
# Date: 2023-11-05
# Runtime: 1114 ms, Memory: 48.8 MB
# Submission Id: 1091723641


class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        n = len(values)
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def recur(node, prev):
            if node and len(graph[node]) == 1:
                return values[node], values[node]
            
            total_sum, total_delete = values[node], 0
            for child in graph[node]:
                if child == prev:
                    continue
                _sum, _delete = recur(child, node)
                total_sum += _sum
                total_delete += _delete
            return total_sum, min(total_delete, values[node])

        total_sum, total_delete = recur(0, -1)
        return total_sum - total_delete