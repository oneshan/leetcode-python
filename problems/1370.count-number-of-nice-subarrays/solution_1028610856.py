# 1370 - Count Number of Nice Subarrays
# Date: 2023-08-22
# Runtime: 726 ms, Memory: 25.2 MB
# Submission Id: 1028610856


from collections import defaultdict
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odds = defaultdict(int)
        odds[0] = 1
        
        ans = curr = 0
        for num in nums:
            curr += num & 1
            ans += odds[curr - k]
            odds[curr] += 1
        return ans