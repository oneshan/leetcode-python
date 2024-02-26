# 1370 - Count Number of Nice Subarrays
# Date: 2022-09-27
# Runtime: 2225 ms, Memory: 23.3 MB
# Submission Id: 809877996


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