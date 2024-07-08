# 0128 - Longest Consecutive Sequence
# Date: 2024-05-28
# Runtime: 333 ms, Memory: 31.7 MB
# Submission Id: 1270287587


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        ans = 0
        for num in num_set:
            if num-1 not in num_set:
                count = 1
                while num + count in num_set:
                    count += 1
                ans = max(ans, count)

        return ans