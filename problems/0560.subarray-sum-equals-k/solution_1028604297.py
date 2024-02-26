# 0560 - Subarray Sum Equals K
# Date: 2023-08-22
# Runtime: 264 ms, Memory: 20.7 MB
# Submission Id: 1028604297


from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr = ans = 0
        counter = defaultdict(int)
        counter[0] = 1
        for num in nums:
            curr += num
            ans += counter[curr-k]
            counter[curr] += 1
        return ans