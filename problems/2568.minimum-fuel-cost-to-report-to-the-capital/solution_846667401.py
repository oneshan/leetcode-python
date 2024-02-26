# 2568 - Minimum Fuel Cost to Report to the Capital
# Date: 2022-11-20
# Runtime: 2265 ms, Memory: 180.5 MB
# Submission Id: 846667401


from collections import defaultdict, deque

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        if not roads:
            return 0
        
        graph = defaultdict(list)
        for x, y in roads:
            graph[x].append(y)
            graph[y].append(x)
        
        tree = defaultdict(list)
        queue = deque([0])
        seen = set([0])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                for child in graph[node]:
                    if child not in seen:
                        seen.add(child)
                        tree[node].append(child)
                        queue.append(child)
        
        ans = 0
        def recur(node):
            nonlocal ans
            if node not in tree:
                return 1
            
            count = 0
            for child in tree[node]:
                tmp = recur(child)
                ans += 1 + (tmp-1) // seats
                count += tmp
            return 1 + count
            
        recur(0)
        return ans