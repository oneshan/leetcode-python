# 0332 - Reconstruct Itinerary
# Date: 2023-09-14
# Runtime: 96 ms, Memory: 17 MB
# Submission Id: 1049285835


from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        graph = defaultdict(list)
        for _from, _to in tickets:
            graph[_from].append(_to)
            
        visited_mask = {}
        for city in graph:
            graph[city].sort()
            visited_mask[city] = 0
        
        n = len(tickets)
        ans = []
        
        def backtracking(city, path):
            nonlocal ans
            
            if len(path) == n + 1:
                ans = path
                return True
            
            for idx, neighbor in enumerate(graph[city]):
                if visited_mask[city] & (1 << idx):
                    continue
                path.append(neighbor)
                visited_mask[city] |= (1 << idx)
                has_result = backtracking(neighbor, path)
                if has_result:
                    return True
                visited_mask[city] ^= (1 << idx)
                path.pop()
            return False
        
        backtracking('JFK', ['JFK'])
        return ans