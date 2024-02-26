# 0278 - First Bad Version
# Date: 2022-12-18
# Runtime: 57 ms, Memory: 13.8 MB
# Submission Id: 861691983


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return right