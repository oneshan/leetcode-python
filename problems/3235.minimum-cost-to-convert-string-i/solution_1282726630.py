# 3235 - Minimum Cost to Convert String I
# Date: 2024-06-09
# Runtime: 2502 ms, Memory: 18.3 MB
# Submission Id: 1282726630


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = defaultdict(list)
        for start, end, c in zip(original, changed, cost):
            graph[start].append((end, c))
        
        @cache
        def get_dist(c1, c2):
            heap = [(0, c1)]
            seen = {c1: 0}
            while heap:
                curr_cost, ch = heapq.heappop(heap)
                if ch == c2:
                    return curr_cost
                for next_ch, next_cost in graph[ch]:
                    if next_ch not in seen or seen[next_ch] > curr_cost + next_cost:
                        seen[next_ch] = curr_cost + next_cost
                        heapq.heappush(heap, (curr_cost+next_cost, next_ch))
            return -1

        ans = 0
        for c1, c2 in zip(source, target):
            if c1 == c2:
                continue
            dist = get_dist(c1, c2)
            if dist == -1:
                return -1
            ans += dist

        return ans