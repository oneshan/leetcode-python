# 0833 - Bus Routes
# Date: 2023-11-12
# Runtime: 467 ms, Memory: 52.6 MB
# Submission Id: 1097125447


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if target == source:
            return 0
        
        graph = defaultdict(set)
        for bus, route in enumerate(routes):
            for stop in route:
                graph[stop].add(bus)
        
        queue = deque([source])
        bus_seen = set()
        stop_seen = {source}
        ans = 0
        while queue:
            for _ in range(len(queue)):
                stop = queue.popleft()
                if stop == target:
                    return ans
                for next_bus in graph[stop]:
                    if next_bus in bus_seen:
                        continue
                    bus_seen.add(next_bus)
                    for next_stop in routes[next_bus]:
                        if next_stop in stop_seen:
                            continue
                        stop_seen.add(next_stop)
                        queue.append(next_stop)
            ans += 1
        return -1