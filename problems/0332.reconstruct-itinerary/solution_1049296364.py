# 0332 - Reconstruct Itinerary
# Date: 2023-09-14
# Runtime: 71 ms, Memory: 16.4 MB
# Submission Id: 1049296364


from collections import defaultdict, deque

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        graph = defaultdict(list)
        out_degree = defaultdict(int)
        for _from, _to in tickets:
            graph[_from].append(_to)
            out_degree[_from] += 1
            
        for city in graph:
            graph[city].sort(reverse=True)
        
        ans = deque()
        stack = ['JFK']
        while stack:
            node = stack[-1]
            if out_degree[node] == 0:
                ans.appendleft(stack.pop())
            else:
                stack.append(graph[node].pop())
                out_degree[node] -= 1

        return ans