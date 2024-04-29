# 0514 - Freedom Trail
# Date: 2024-04-28
# Runtime: 2387 ms, Memory: 16.6 MB
# Submission Id: 1244164054


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:

        dp = [0] * len(ring)
        for ki in range(len(key)-1, -1, -1):
            new_dp = [float('inf')] * len(ring)
            for ri in range(len(ring)):
                for idx, ch in enumerate(ring):
                    if ch == key[ki]:
                        min_dist = min(
                            abs(idx-ri),
                            len(ring) - abs(idx-ri),
                        )
                        new_dp[ri] = min(new_dp[ri], min_dist + 1 + dp[idx])
            dp = new_dp

        return dp[0]