# 1675 - Magnetic Force Between Two Balls
# Date: 2024-06-20
# Runtime: 907 ms, Memory: 30.1 MB
# Submission Id: 1294308621


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()

        def is_valid(diff):
            count = 1
            prev = position[0]
            for i in range(1, n):
                if position[i] - prev >= diff:
                    count += 1
                    prev = position[i]
                    if count == m:
                        return True
            return False

        res = -1
        left, right = 0, position[-1] - position[0]
        while left <= right:
            mid = (left + right) // 2
            if is_valid(mid):
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res