# 0278 - First Bad Version
# Date: 2022-07-16
# Runtime: 46 ms, Memory: 13.9 MB
# Submission Id: 748346014


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left+right) // 2
            is_bad = isBadVersion(mid)
            if is_bad:
                right = mid
            else:
                left = mid + 1
        return left