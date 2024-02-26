# 0300 - Longest Increasing Subsequence
# Date: 2022-11-09
# Runtime: 1063 ms, Memory: 14.3 MB
# Submission Id: 839908064


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = []
        for num in nums:
            for i in range(len(lis)):
                if num <= lis[i]:
                    lis[i] = num
                    break
            else:
                lis.append(num)
        return len(lis)