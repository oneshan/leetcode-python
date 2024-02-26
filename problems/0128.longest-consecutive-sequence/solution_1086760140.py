# 0128 - Longest Consecutive Sequence
# Date: 2023-10-29
# Runtime: 376 ms, Memory: 31.4 MB
# Submission Id: 1086760140


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = set(nums)
        ans = 1
        for num in nums:
            if num - 1 in nums:
                continue
            count = 1
            while num + count in nums:
                count += 1
            ans = max(ans, count)
        return ans