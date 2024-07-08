# 3383 - Taking Maximum Energy From the Mystic Dungeon
# Date: 2024-05-12
# Runtime: 1172 ms, Memory: 30.5 MB
# Submission Id: 1255934764


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        ans = float('-inf')

        for i in range(n-1, -1, -1):
            if i + k < n:
                energy[i] += energy[i+k]
            ans = max(ans, energy[i])
        return ans