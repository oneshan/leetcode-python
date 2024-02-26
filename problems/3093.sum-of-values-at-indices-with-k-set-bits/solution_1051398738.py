# 3093 - Sum of Values at Indices With K Set Bits
# Date: 2023-09-17
# Runtime: 76 ms, Memory: 16.5 MB
# Submission Id: 1051398738


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        
        def get_bits(num):
            count = 0
            while num:
                count += 1
                num &= (num-1)
            return count
        
        ans = 0
        for idx, num in enumerate(nums):
            if get_bits(idx) == k:
                ans += num
        return ans