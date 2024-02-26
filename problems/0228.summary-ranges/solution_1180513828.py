# 0228 - Summary Ranges
# Date: 2024-02-20
# Runtime: 32 ms, Memory: 16.5 MB
# Submission Id: 1180513828


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i, n = 0, len(nums)
        ans = []
        while i < n:
            start = nums[i]
            while i + 1 < n and nums[i] + 1 == nums[i+1]:
                i += 1
            
            if start == nums[i]:
                ans.append(f"{start}")
            else:
                ans.append(f"{start}->{nums[i]}")
            i += 1
        return ans