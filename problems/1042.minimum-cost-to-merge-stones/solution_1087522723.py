# 1042 - Minimum Cost to Merge Stones
# Date: 2023-10-30
# Runtime: 48 ms, Memory: 16.6 MB
# Submission Id: 1087522723


class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if (n-1) % (k-1):
            return -1

        prefix_sum = [0] * (n+1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + stones[i]
        
        @cache
        def recur(left, right): 
            """Return min cost of merging stones[left:right]."""
            if right - left < k:
                return 0
            
            ans = float('inf')
            for mid in range(left+1, right, k-1):
                ans = min(ans, recur(left, mid) + recur(mid, right))
            if (right - left - 1) % (k-1) == 0:
                ans += prefix_sum[right] - prefix_sum[left]
            return ans 
        
        return recur(0, n)