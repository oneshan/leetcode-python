# 3383 - Taking Maximum Energy From the Mystic Dungeon
# Date: 2024-05-12
# Runtime: 1159 ms, Memory: 30 MB
# Submission Id: 1255889349


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        ans = float('-inf')
        
        seen = [False] * n
        for i in range(n):
            if seen[i]:
                continue
            curr = 0
            while i < n:
                seen[i] = True
                curr = max(curr, 0) + energy[i]
                i += k
            ans = max(ans, curr)
        return ans
                