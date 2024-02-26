# 0300 - Longest Increasing Subsequence
# Date: 2023-09-21
# Runtime: 66 ms, Memory: 16.6 MB
# Submission Id: 1055519395


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = []
        for num in nums:
            left, right = 0, len(lis)
            while left < right:
                mid = (left + right) // 2
                if lis[mid] >= num:
                    right = mid
                else:
                    left = mid + 1
            if left == len(lis):
                lis.append(num)
            else:
                lis[left] = num
        return len(lis)