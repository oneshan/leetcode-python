# 3292 - Earliest Second to Mark Indices I
# Date: 2024-02-25
# Runtime: 110 ms, Memory: 16.9 MB
# Submission Id: 1185507145


class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        n = len(nums)
        m = len(changeIndices)

        required = sum(nums) + n
        if required > m:
            return -1

        def check(second):
            required = 0
            seen = set()
            for i in range(second, -1, -1):
                idx = changeIndices[i] - 1
                if idx not in seen:
                    required += nums[idx]
                    seen.add(idx)
                elif required:
                    required -= 1
            if len(seen) < n:
                return False
            return required == 0
        
        left, right = 0, m
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left + 1 if left < m else -1