# 0966 - Binary Subarrays With Sum
# Date: 2023-08-29
# Runtime: 264 ms, Memory: 20.3 MB
# Submission Id: 1035169686


from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        
        curr = ans = 0
        for num in nums:
            curr += num
            ans += count[curr - goal]
            count[curr] += 1
        return ans