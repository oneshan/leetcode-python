# 2681 - Put Marbles in Bags
# Date: 2023-07-08
# Runtime: 784 ms, Memory: 30.1 MB
# Submission Id: 988992661


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        pair = [0] * (n-1)
        for i in range(n-1):
            pair[i] = weights[i] + weights[i+1]
        pair.sort()
        
        ans = 0
        for i in range(k-1):
            ans += pair[n-2-i] - pair[i]
        
        return ans