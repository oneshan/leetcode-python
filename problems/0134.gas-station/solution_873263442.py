# 0134 - Gas Station
# Date: 2023-01-07
# Runtime: 714 ms, Memory: 19.3 MB
# Submission Id: 873263442


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        
        if sum(gas) - sum(cost) < 0:
            return -1
        
        curr = start_idx = 0
        for i in range(n):
            curr += gas[i] - cost[i]
            if curr < 0:
                start_idx = i+1
                curr = 0
        return start_idx