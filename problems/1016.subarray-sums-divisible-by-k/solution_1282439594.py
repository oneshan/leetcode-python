# 1016 - Subarray Sums Divisible by K
# Date: 2024-06-09
# Runtime: 295 ms, Memory: 21.4 MB
# Submission Id: 1282439594


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        counter = Counter()
        counter[0] = 1

        ans = curr = 0
        for num in nums:
            curr = (curr + num) % k
            ans += counter[curr]
            counter[curr] += 1
        return ans