# 0300 - Longest Increasing Subsequence
# Date: 2024-05-25
# Runtime: 76 ms, Memory: 16.9 MB
# Submission Id: 1267275155


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        lis = []

        for num in nums:

            # idx = bisect.bisect_left(lis, num)
            idx = n
            left, right = 0, len(lis)-1
            while left <= right:
                mid = (left + right) // 2
                if num <= lis[mid]:
                    idx = mid
                    right = mid - 1
                else:
                    left = mid + 1

            if idx < len(lis):
                lis[idx] = num
            else:
                lis.append(num)

        print(lis)
        return len(lis)