# 3183 - Find the K-or of an Array
# Date: 2023-10-29
# Runtime: 101 ms, Memory: 16.3 MB
# Submission Id: 1086457673


class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        bits = [0] * 32
        for num in nums:
            for i in range(32):
                mask = 1 << i
                if mask & num:
                    bits[i] += 1
        
        ans = 0
        for i in range(32):
            if bits[i] >= k:
                ans += (1 << i)
        return ans