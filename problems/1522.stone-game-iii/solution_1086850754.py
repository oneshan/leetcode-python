# 1522 - Stone Game III
# Date: 2023-10-29
# Runtime: 1752 ms, Memory: 20.4 MB
# Submission Id: 1086850754


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        total = 0
        dp = [0] * 3
        for i in range(n-1, -1, -1):
            total += stoneValue[i]
            dp[i % 3] = total - min([dp[(i+j) % 3] for j in range(1, 4)])
        
        alice, bob = dp[0], total - dp[0]
        if alice == bob:
            return 'Tie'
        return 'Alice' if alice > bob else 'Bob'