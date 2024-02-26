# 0332 - Reconstruct Itinerary
# Date: 2022-10-20
# Runtime: 205 ms, Memory: 15.1 MB
# Submission Id: 826438350


from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        visited_mask = {}
        for _from, _to in tickets:
            graph[_from].append(_to)
        for key, value in graph.items():
            value.sort()
            visited_mask[key] = 0
        
        n = len(tickets)
        ans = []
        
        def backtracking(node, path):
            nonlocal ans
            if len(path) == n+1:
                ans = path
                return True
            for idx, neighbor in enumerate(graph[node]):
                mask = 1 << idx
                if visited_mask[node] & mask:
                    continue
                visited_mask[node] |= mask
                has_result = backtracking(neighbor, path+[neighbor])
                visited_mask[node] ^= mask
                if has_result:
                    return True
            return False
        
        backtracking('JFK', ['JFK'])
        return ans
        