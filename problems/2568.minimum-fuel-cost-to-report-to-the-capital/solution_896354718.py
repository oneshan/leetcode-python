# 2568 - Minimum Fuel Cost to Report to the Capital
# Date: 2023-02-12
# Runtime: 2021 ms, Memory: 159.5 MB
# Submission Id: 896354718


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        if not roads:
            return 0
        
        graph = defaultdict(list)
        for x, y in roads:
            graph[x].append(y)
            graph[y].append(x)
                
        ans = 0
        def recur(node, parent):
            nonlocal ans
            count = 1
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                count += recur(neighbor, node)
            if node:
                ans += 1 + (count-1) // seats
            return count
        
        recur(0, -1)
        return ans