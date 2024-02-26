# 0300 - Longest Increasing Subsequence
# Date: 2024-02-12
# Runtime: 65 ms, Memory: 17.1 MB
# Submission Id: 1172710964


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = []
        for num in nums:
            idx = bisect.bisect_left(lis, num)
            if idx < len(lis):
                lis[idx] = num
            else:
                lis.append(num)
        return len(lis)