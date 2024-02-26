# 2568 - Minimum Fuel Cost to Report to the Capital
# Date: 2022-11-26
# Runtime: 2010 ms, Memory: 159.4 MB
# Submission Id: 850095351


from collections import defaultdict, deque

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
                ans += math.ceil(count / seats)
            return count
        
        recur(0, -1)
        return ans