# 0128 - Longest Consecutive Sequence
# Date: 2023-10-29
# Runtime: 389 ms, Memory: 36.6 MB
# Submission Id: 1086756643


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        ans = 1
        nums = set(nums)
        seen = set()
        for num in nums:
            if num in seen:
                continue
            count = 1
            while num + count in nums:
                count += 1
                seen.add(num + count)
            ans = max(ans, count)
        return ans