# 0561 - Array Partition
# Date: 2022-07-14
# Runtime: 693 ms, Memory: 16.8 MB
# Submission Id: 746961404


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        k = 10000
        
        bucket = [0] * (2*k+1)
        for num in nums:
            bucket[num+k] += 1
        
        ans = 0
        is_even = True
        for num in range(2*k+1):
            while bucket[num] > 0:
                if is_even:
                    ans += num -k
                is_even ^= 1
                bucket[num] -= 1
        return ans