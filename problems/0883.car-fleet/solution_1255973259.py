# 0883 - Car Fleet
# Date: 2024-05-12
# Runtime: 679 ms, Memory: 39 MB
# Submission Id: 1255973259


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for p, s in sorted(zip(position, speed)):
            time = (target - p) / s
            while stack and stack[-1] <= time:
                stack.pop()
            stack.append(time)
        return len(stack)