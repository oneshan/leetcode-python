# 3292 - Earliest Second to Mark Indices I
# Date: 2024-02-25
# Runtime: 124 ms, Memory: 16.9 MB
# Submission Id: 1185509366


class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        n = len(nums)
        m = len(changeIndices)

        required = sum(nums) + n
        if required > m:
            return -1

        def check(second):
            mask = required = 0
            for i in range(second, -1, -1):
                idx = changeIndices[i] - 1
                if mask & 1 << idx == 0:
                    mask |= 1 << idx
                    required += nums[idx]
                elif required:
                    required -= 1
            return mask == (1 << n) - 1 and required == 0
        
        left, right = 0, m
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left + 1 if left < m else -1