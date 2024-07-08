# 0332 - Reconstruct Itinerary
# Date: 2024-05-22
# Runtime: 65 ms, Memory: 16.9 MB
# Submission Id: 1264727219


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for _from, _to in tickets:
            graph[_from].append(_to)
        for _from in graph:
            graph[_from].sort(reverse=True)
        
        n = len(tickets)
        ans = []
        stack = ['JFK']
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            ans.append(stack.pop())

        return ans[::-1]