# 3238 - Minimum Cost to Convert String II
# Date: 2023-12-24
# Runtime: 1751 ms, Memory: 20.9 MB
# Submission Id: 1127120123


from collections import defaultdict
import heapq

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        mapping = defaultdict(list)
        prefix = defaultdict(list)
        for o_str, n_str, cost_str in zip(original, changed, cost):
            mapping[o_str].append((n_str, cost_str))
            prefix[o_str[0]].append(o_str)
        
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

        len_s = len(source)

        @cache
        def dp(i):
            if i == len_s:
                return 0
            
            next_cost = float('inf')
            if source[i] == target[i]:
                next_cost = dp(i+1)
                
            if source[i] in prefix:
                for candidate in prefix[source[i]]:
                    if source[i:i+len(candidate)] != candidate:
                        continue
                    cost = traverse(candidate, target[i:i+len(candidate)])
                    if cost == -1:
                        continue
                    next_cost = min(next_cost, cost + dp(i+len(candidate)))
            return next_cost
        
        ans = dp(0)
        return ans if ans != float('inf') else -1