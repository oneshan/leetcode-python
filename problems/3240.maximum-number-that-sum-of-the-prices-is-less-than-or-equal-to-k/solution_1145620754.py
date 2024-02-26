# 3240 - Maximum Number That Sum of the Prices Is Less Than or Equal to K
# Date: 2024-01-14
# Runtime: 244 ms, Memory: 17.3 MB
# Submission Id: 1145620754


class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        
        def get_count(num):
            res = 0
            for i in range(x, num.bit_length()+1, x):
                q, r = divmod(num+1, 1 << i)
                size = 1 << (i-1)
                res += q * size + max(0, r - size)
            return res
        
        left, right = 1, 1 << 64
        while left < right:
            mid = (left + right) // 2
            if get_count(mid) <= k:
                left = mid + 1
            else:
                right = mid
        return left - 1