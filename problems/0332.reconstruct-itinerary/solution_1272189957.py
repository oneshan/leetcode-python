# 0332 - Reconstruct Itinerary
# Date: 2024-05-30
# Runtime: 77 ms, Memory: 16.7 MB
# Submission Id: 1272189957


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for _from, _to in tickets:
            graph[_from].append(_to)
        for _from in graph:
            heapq.heapify(graph[_from])
        
        ans = []

        def dfs(city):
            while graph[city]:
                next_city = heapq.heappop(graph[city])
                dfs(next_city)
            ans.append(city)

        dfs('JFK')
        return ans[::-1]