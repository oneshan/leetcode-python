# 0300 - Longest Increasing Subsequence
# Date: 2024-05-25
# Runtime: 56 ms, Memory: 16.6 MB
# Submission Id: 1267275325


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        lis = []

        for num in nums:

            # idx = bisect.bisect_left(lis, num)
            idx = n
            left, right = 0, len(lis)
            while left < right:
                mid = (left + right) // 2
                if num <= lis[mid]:
                    right = mid
                else:
                    left = mid + 1
            idx = left

            if idx < len(lis):
                lis[idx] = num
            else:
                lis.append(num)

        print(lis)
        return len(lis)