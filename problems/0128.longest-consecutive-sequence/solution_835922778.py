# 0128 - Longest Consecutive Sequence
# Date: 2022-11-03
# Runtime: 861 ms, Memory: 29.1 MB
# Submission Id: 835922778


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = set(nums)
        ans = 0
        for num in nums:
            if num-1 in nums:
                continue
            curr_num, curr_len = num, 1
            while curr_num + 1 in nums:
                curr_num += 1
                curr_len += 1
            ans = max(ans, curr_len)
        return ans