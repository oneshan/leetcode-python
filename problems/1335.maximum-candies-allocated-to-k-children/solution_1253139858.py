# 1335 - Maximum Candies Allocated to K Children
# Date: 2024-05-09
# Runtime: 1137 ms, Memory: 29.9 MB
# Submission Id: 1253139858


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        candies.sort()

        def check(num):
            count = 0
            for candy in candies:
                count += candy // num
                if count >= k:
                    return True
            return False

        left, right = 0, candies[-1]
        while left < right:
            mid = (left + right + 1) // 2
            if check(mid):
                left = mid
            else:
                right = mid - 1

        return left