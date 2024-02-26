# 1290 - Make Array Strictly Increasing
# Date: 2023-06-17
# Runtime: 915 ms, Memory: 153.2 MB
# Submission Id: 973160292


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        m, n = len(arr1), len(arr2)
        
        @cache
        def dp(i, prev):
            if i == m:
                return 0
            cost = float('inf')
            if arr1[i] > prev:
                cost = dp(i+1, arr1[i])
            j = bisect.bisect_right(arr2, prev)
            if j < n:
                cost = min(cost, 1 + dp(i+1, arr2[j]))        
            return cost
        
        ans = dp(0, -1)
        return ans if ans < float('inf') else -1