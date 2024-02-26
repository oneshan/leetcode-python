# 3235 - Minimum Cost to Convert String I
# Date: 2023-12-24
# Runtime: 3103 ms, Memory: 19.2 MB
# Submission Id: 1127050375


from collections import defaultdict
import heapq

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        mapping = defaultdict(list)
        
        for o_ch, n_ch, cost_ch in zip(original, changed, cost):
            mapping[o_ch].append((n_ch, cost_ch))
        
        @cache
        def traverse(_from, _to):
            distances = {}
            distances[_from] = 0
            
            heap = [(0, _from)]
            while heap:
                cost, ch = heapq.heappop(heap)
                if ch == _to:
                    return cost
                if cost > distances.get(ch, float('inf')):
                    continue
                for next_ch, next_cost in mapping[ch]:
                    new_cost = cost+next_cost
                    if new_cost < distances.get(next_ch, float('inf')):
                        distances[next_ch] = new_cost
                        heapq.heappush(heap, (new_cost, next_ch))
            return -1
        
        ans = 0
        for c1, c2 in zip(source, target):
            if c1 == c2:
                continue
            cost = traverse(c1, c2)
            if cost == -1:
                return -1
            ans += cost
        return ans