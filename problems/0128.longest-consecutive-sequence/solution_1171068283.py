# 0128 - Longest Consecutive Sequence
# Date: 2024-02-10
# Runtime: 4434 ms, Memory: 31.8 MB
# Submission Id: 1171068283


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        ans = 0
        for num in nums:
            if num-1 not in num_set:
                curr = num
                while curr + 1 in num_set:
                    curr += 1
                ans = max(ans, curr - num + 1)

        return ans