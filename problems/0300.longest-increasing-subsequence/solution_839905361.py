# 0300 - Longest Increasing Subsequence
# Date: 2022-11-09
# Runtime: 162 ms, Memory: 14.2 MB
# Submission Id: 839905361


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = []

        for num in nums:

            left, right = 0, len(lis)
            while left < right:
                mid = (left + right) // 2
                if num > lis[mid]:
                    left = mid + 1
                else:
                    right = mid
                    
            if left == len(lis):
                lis.append(num)
            else:
                lis[left] = num

        return len(lis)