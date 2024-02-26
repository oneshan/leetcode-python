# 0128 - Longest Consecutive Sequence
# Date: 2024-02-10
# Runtime: 4491 ms, Memory: 32 MB
# Submission Id: 1171068523


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        ans = 0
        for num in nums:
            if num-1 not in num_set:
                count = 0
                while num + count in num_set:
                    count += 1
                ans = max(ans, count)

        return ans