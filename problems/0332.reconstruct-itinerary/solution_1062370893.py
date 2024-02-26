# 0332 - Reconstruct Itinerary
# Date: 2023-09-29
# Runtime: 85 ms, Memory: 16.8 MB
# Submission Id: 1062370893


from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        visited_mask = {}
        for _from, _to in tickets:
            graph[_from].append(_to)
        for key, value in graph.items():
            value.sort(reverse=True)
            visited_mask[key] = 0
        
        n = len(tickets)
        ans = []
        
        def dfs(city):
            nonlocal ans
            while graph[city]:
                dfs(graph[city].pop())
            ans.append(city)
            
        dfs('JFK')
        return ans[::-1]