# 0510 - Count Subarrays With More Ones Than Zeros
# Date: 2024-06-11
# Runtime: 1156 ms, Memory: 23.3 MB
# Submission Id: 1284900673


class BITTree:
    def __init__(self, size):
        self.size = size
        self.bits = [0] * (size+1)

    def update(self, idx, num):
        idx += 1
        while idx <= self.size:
            self.bits[idx] += num
            idx += idx & -idx
    
    def get_sum(self, idx):
        idx += 1
        res = 0
        while idx > 0:
            res += self.bits[idx]
            idx -= idx & -idx
        return res

class Solution:
    def subarraysWithMoreZerosThanOnes(self, nums: List[int]) -> int:
        MOD = 1_000_000_007

        prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix[i+1] = prefix[i] + (1 if nums[i] else -1)

        offset = min(prefix)
        size = max(prefix) - offset + 1
        bit = BITTree(size)
        
        ans = 0
        for p in prefix:
            ans += bit.get_sum(p-offset-1)
            bit.update(p-offset, 1)
        return ans % MOD