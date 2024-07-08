# 0134 - Gas Station
# Date: 2024-05-30
# Runtime: 933 ms, Memory: 22.1 MB
# Submission Id: 1272134034


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        ans = curr = total = 0
        for i in range(n):
            total += gas[i] - cost[i]
            curr += gas[i] - cost[i]
            if curr < 0:
                curr = 0
                ans = i+1
        return ans if total >= 0 else -1