# 2471 - Minimum Amount of Time to Collect Garbage
# Date: 2023-11-20
# Runtime: 880 ms, Memory: 39.2 MB
# Submission Id: 1102697078


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        n = len(garbage)
        ans = 0
        seen = set()
        for i in range(n-1, -1, -1):
            for g in garbage[i]:
                seen.add(g)
                ans += 1
            if i:
                ans += travel[i-1] * len(seen)
        return ans