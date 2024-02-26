# 0993 - Tallest Billboard
# Date: 2023-06-24
# Runtime: 582 ms, Memory: 16.9 MB
# Submission Id: 978474395


class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        n = len(rods)
        
        dp = {0: 0}
        for rod in rods:
            new_dp = dp.copy()
            for diff, taller in dp.items():
                shorter = taller - diff
                new_dp[diff + rod] = max(new_dp.get(diff+rod, 0), taller + rod)
                new_diff = abs(shorter + rod - taller)
                new_taller = max(taller, shorter + rod)
                new_dp[new_diff] = max(new_dp.get(new_diff, 0), new_taller)
            dp = new_dp
        return dp.get(0, 0)