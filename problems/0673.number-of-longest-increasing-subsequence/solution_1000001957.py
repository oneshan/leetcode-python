# 0673 - Number of Longest Increasing Subsequence
# Date: 2023-07-21
# Runtime: 1127 ms, Memory: 16.5 MB
# Submission Id: 1000001957


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        max_len = 0
        
        length, count = [1] * n, [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[i] < length[j] + 1: 
                        length[i], count[i] = length[j] + 1, count[j]
                    elif length[i] == length[j] + 1:
                        count[i] += count[j]
            max_len = max(max_len, length[i])
        
        ans = 0
        for i in range(n):
            if length[i] == max_len:
                ans += count[i]
        return ans