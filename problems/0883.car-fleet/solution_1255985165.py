# 0883 - Car Fleet
# Date: 2024-05-12
# Runtime: 635 ms, Memory: 38.9 MB
# Submission Id: 1255985165


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ans = 0

        bottleneck = float('-inf')
        for p, s in sorted(zip(position, speed), reverse=True):
            time = (target - p) / s
            if time > bottleneck:
                bottleneck = time
                ans += 1
        return ans