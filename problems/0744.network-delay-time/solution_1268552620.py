# 0744 - Network Delay Time
# Date: 2024-05-26
# Runtime: 361 ms, Memory: 18.4 MB
# Submission Id: 1268552620


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for _from, _to, cost in times:
            graph[_from].append((cost, _to))
        
        heap = [(0, k)]
        visited = set()
        ans = 0

        while heap:
            curr_cost, city = heapq.heappop(heap)
            if city in visited:
                continue
            
            visited.add(city)
            if len(visited) == n:
                return curr_cost

            for next_cost, next_city in graph[city]:
                if next_city not in visited:
                    heapq.heappush(heap, (curr_cost+next_cost, next_city))

        return ans if len(visited) == n else -1