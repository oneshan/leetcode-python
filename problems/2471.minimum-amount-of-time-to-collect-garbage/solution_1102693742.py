# 2471 - Minimum Amount of Time to Collect Garbage
# Date: 2023-11-20
# Runtime: 855 ms, Memory: 42.4 MB
# Submission Id: 1102693742


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        
        n = len(garbage)
        for i in range(1, n-1):
            travel[i] += travel[i-1]
        
        cost = 0
        last_seen = defaultdict(int)
        for i in range(n):
            for ch in garbage[i]:
                cost += 1
                last_seen[ch] = i
        
        for i in last_seen.values():
            if i:
                cost += travel[i-1]
        return cost