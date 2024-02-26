# 0332 - Reconstruct Itinerary
# Date: 2023-09-14
# Runtime: 90 ms, Memory: 16.9 MB
# Submission Id: 1049291747


from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        graph = defaultdict(list)
        for _from, _to in tickets:
            graph[_from].append(_to)
            
        for city in graph:
            graph[city].sort(reverse=True)
        
        ans = []
        
        def dfs(city):
            nonlocal ans
            while graph[city]:
                dfs(graph[city].pop())
            ans.append(city)
            
        
        dfs('JFK')
        return ans[::-1]