# 0510 - Count Subarrays With More Ones Than Zeros
# Date: 2024-06-11
# Runtime: 673 ms, Memory: 30.9 MB
# Submission Id: 1284863336


class Solution:
    def subarraysWithMoreZerosThanOnes(self, nums: List[int]) -> int:
        MOD = 1_000_000_007

        counter = Counter()
        counter[0] = 1

        # cnt = the count of subarrays ending at i
        ans = cnt = curr = 0
        for num in nums:
            if num:
                cnt += counter[curr]
            else:
                cnt -= counter[curr-1]
            curr += (1 if num else -1)
            counter[curr] += 1
            ans += cnt % MOD

        return ans % MOD