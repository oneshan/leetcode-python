# 2472 - Build a Matrix With Conditions
# Date: 2024-07-21
# Runtime: 579 ms, Memory: 25.7 MB
# Submission Id: 1328113475


class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        def topo(conditions):            
            graph = defaultdict(list)
            in_degree = [0] * (1+k)
            for _from, _to in conditions:
                graph[_from].append(_to)
                in_degree[_to] += 1

            res = []
            queue = deque([i for i in range(1, 1+k) if in_degree[i] == 0])
            while queue:
                node = queue.popleft()
                res.append(node)
                for neighbor in graph[node]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)
            return res

        rows = topo(rowConditions)
        cols = topo(colConditions)
        if len(rows) != k or len(cols) != k:
            return []

        res = [[0] * k for _ in range(k)]
        val_to_ridx = {val: ri for ri, val in enumerate(rows)}        
        for ci, val, in enumerate(cols):
            ri = val_to_ridx[val]
            res[ri][ci] = val
        return res