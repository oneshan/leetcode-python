# 1488 - Sort Integers by The Power Value
# Date: 2022-11-26
# Runtime: 392 ms, Memory: 29 MB
# Submission Id: 849884133


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {}
        
        def get_power_value(num):
            if num == 1:
                return 1
            if num not in memo:
                if num & 1:
                    memo[num] = 1 + get_power_value(3 * num + 1)
                else:
                    memo[num] = 1 + get_power_value(num>>1)
            return memo[num]
        
        candidate = []
        for i in range(lo, hi+1):
            candidate.append((get_power_value(i), i))
        
        return sorted(candidate)[k-1][1]
        
        